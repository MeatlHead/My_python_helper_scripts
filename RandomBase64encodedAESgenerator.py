from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

def generate_aes_key():
    # Generate a random AES key (256 bits)
    return os.urandom(32)

def encrypt_aes_key(aes_key, key_to_encrypt):
    # Initialize AES cipher
    cipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the key
    encrypted_key = encryptor.update(key_to_encrypt) + encryptor.finalize()

    return encrypted_key

def main():
    # Generate a random AES decryption key
    aes_decryption_key = generate_aes_key()

    # Sample key to be encrypted
    key_to_encrypt = b"SecretKey123"

    # Encrypt the sample key using AES
    encrypted_key = encrypt_aes_key(aes_decryption_key, key_to_encrypt)

    # Base64-encode the encrypted key
    base64_encoded_encrypted_key = base64.b64encode(encrypted_key).decode()

    print("AES Decryption Key:", aes_decryption_key)
    print("Base64-encoded Encrypted Key:", base64_encoded_encrypted_key)

if __name__ == "__main__":
    main()
