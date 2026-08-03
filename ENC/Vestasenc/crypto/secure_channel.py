from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class SecureChannel:
    """TLS-like Secure Channel using ECDH + HKDF"""
    
    def __init__(self):
        """Initialize secure channel with ECDH"""
        self.private_key = ec.generate_private_key(
            ec.SECP256R1(), 
            default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.shared_secret = None
        self.symmetric_key = None
    
    def get_public_key_pem(self):
        """Export public key as PEM"""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicKeyFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
    
    def establish_channel(self, peer_public_key_pem):
        """Establish secure channel with peer"""
        # Load peer's public key
        peer_public_key = serialization.load_pem_public_key(
            peer_public_key_pem.encode('utf-8'),
            backend=default_backend()
        )
        
        # Perform ECDH
        self.shared_secret = self.private_key.exchange(
            ec.ECDH(), 
            peer_public_key
        )
        
        # Derive symmetric key using HKDF
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'secure-channel',
            backend=default_backend()
        )
        self.symmetric_key = hkdf.derive(self.shared_secret)
        
        return True
    
    def encrypt_message(self, plaintext):
        """Encrypt message using derived key"""
        if not self.symmetric_key:
            raise Exception("Channel not established")
        
        iv = get_random_bytes(16)
        cipher = AES.new(self.symmetric_key, AES.MODE_CBC, iv)
        padded = pad(plaintext.encode('utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded)
        
        return base64.b64encode(iv + ciphertext).decode('utf-8')
    
    def decrypt_message(self, ciphertext):
        """Decrypt message using derived key"""
        if not self.symmetric_key:
            raise Exception("Channel not established")
        
        raw = base64.b64decode(ciphertext)
        iv = raw[:16]
        encrypted_data = raw[16:]
        
        cipher = AES.new(self.symmetric_key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        
        return decrypted.decode('utf-8')

