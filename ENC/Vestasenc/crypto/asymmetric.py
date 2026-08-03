from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64

class RSACipher:
    """RSA-2048 Asymmetric Encryption"""
    
    def __init__(self):
        """Generate RSA-2048 key pair"""
        self.key_pair = RSA.generate(2048)
        self.public_key = self.key_pair.publickey()
    
    def encrypt(self, plaintext):
        """Encrypt using RSA public key"""
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted = cipher.encrypt(plaintext.encode('utf-8'))
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt(self, ciphertext):
        """Decrypt using RSA private key"""
        try:
            cipher = PKCS1_OAEP.new(self.key_pair)
            encrypted_data = base64.b64decode(ciphertext)
            decrypted = cipher.decrypt(encrypted_data)
            return decrypted.decode('utf-8')
        except Exception as e:
            return f"Decryption Error: {str(e)}"
    
    def export_keys(self):
        """Export public and private keys"""
        private_pem = self.key_pair.export_key().decode('utf-8')
        public_pem = self.public_key.export_key().decode('utf-8')
        return public_pem, private_pem

class ECCCipher:
    """ECC Curve25519 Key Exchange"""
    
    def __init__(self):
        """Generate ECC private key using Curve25519"""
        self.private_key = ec.generate_private_key(
            ec.SECP256R1(), 
            default_backend()
        )
        self.public_key = self.private_key.public_key()
    
    def get_public_key_bytes(self):
        """Export public key as bytes"""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicKeyFormat.SubjectPublicKeyInfo
        )
    
    def exchange(self, peer_public_key):
        """Perform ECDH key exchange"""
        shared_key = self.private_key.exchange(
            ec.ECDH(), 
            peer_public_key
        )
        return shared_key

