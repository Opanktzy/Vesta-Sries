from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

class AESCipher:
    """AES-256-CBC Encryption Implementation"""
    
    def __init__(self, key=None):
        """Initialize AES cipher with 256-bit key"""
        self.key = key if key else get_random_bytes(32)  # 256-bit key
        self.block_size = AES.block_size
    
    def encrypt(self, plaintext):
        """Encrypt plaintext using AES-256-CBC"""
        iv = get_random_bytes(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        # Pad and encrypt
        padded_data = pad(plaintext.encode('utf-8'), self.block_size)
        ciphertext = cipher.encrypt(padded_data)
        
        # Return IV + ciphertext (base64 encoded)
        return base64.b64encode(iv + ciphertext).decode('utf-8')
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using AES-256-CBC"""
        try:
            raw = base64.b64decode(ciphertext)
            iv = raw[:self.block_size]
            encrypted_data = raw[self.block_size:]
            
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            decrypted = unpad(cipher.decrypt(encrypted_data), self.block_size)
            
            return decrypted.decode('utf-8')
        except Exception as e:
            return f"Decryption Error: {str(e)}"
    
    def get_key_hex(self):
        """Get key in hexadecimal format"""
        return self.key.hex()

