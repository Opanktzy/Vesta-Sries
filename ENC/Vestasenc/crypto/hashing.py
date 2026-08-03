import argon2
import hashlib
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

class PasswordHasher:
    """Argon2id Password Hashing"""
    
    def __init__(self):
        """Initialize Argon2 hasher with secure parameters"""
        self.hasher = argon2.PasswordHasher(
            time_cost=3,          # iterations
            memory_cost=65536,    # 64 MB
            parallelism=4,        # threads
            hash_len=32,          # 256-bit output
            salt_len=16,
            type=argon2.low_level.Type.ID
        )
    
    def hash_password(self, password):
        """Hash password using Argon2id"""
        return self.hasher.hash(password)
    
    def verify_password(self, hash_value, password):
        """Verify password against Argon2 hash"""
        try:
            self.hasher.verify(hash_value, password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False
        except Exception:
            return False

class PBKDF2Hasher:
    """PBKDF2-HMAC-SHA256 Key Derivation"""
    
    @staticmethod
    def derive_key(password, salt=None, iterations=100000, key_length=32):
        """Derive key from password using PBKDF2"""
        if salt is None:
            from Crypto.Random import get_random_bytes
            salt = get_random_bytes(16)
        
        key = PBKDF2(
            password, 
            salt, 
            dkLen=key_length,
            count=iterations,
            hmac_hash_module=SHA256
        )
        
        return key, salt

class GeneralHasher:
    """General purpose hashing functions"""
    
    @staticmethod
    def sha256(data):
        """SHA-256 hash"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    @staticmethod
    def sha512(data):
        """SHA-512 hash"""
        return hashlib.sha512(data.encode()).hexdigest()

