from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
import os

class FileEncryptor:
    """File Encryption using AES + Password-based Key Derivation"""
    
    @staticmethod
    def encrypt_file(input_file, output_file, password):
        """Encrypt file with password"""
        # Generate salt
        salt = get_random_bytes(16)
        
        # Derive key from password using PBKDF2
        key = PBKDF2(
            password, 
            salt, 
            dkLen=32,
            count=100000,
            hmac_hash_module=SHA256
        )
        
        # Generate IV
        iv = get_random_bytes(16)
        
        # Read file
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        
        # Encrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(plaintext, AES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        
        # Write encrypted file: salt + iv + ciphertext
        with open(output_file, 'wb') as f:
            f.write(salt)
            f.write(iv)
            f.write(ciphertext)
        
        return True
    
    @staticmethod
    def decrypt_file(input_file, output_file, password):
        """Decrypt file with password"""
        try:
            # Read encrypted file
            with open(input_file, 'rb') as f:
                salt = f.read(16)
                iv = f.read(16)
                ciphertext = f.read()
            
            # Derive key from password
            key = PBKDF2(
                password, 
                salt, 
                dkLen=32,
                count=100000,
                hmac_hash_module=SHA256
            )
            
            # Decrypt
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
            
            # Write decrypted file
            with open(output_file, 'wb') as f:
                f.write(decrypted)
            
            return True
        except Exception as e:
            return False

