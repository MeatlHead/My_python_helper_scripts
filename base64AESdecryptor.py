from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

def decrypt_aes_key(base64_encrypted_key, decryption_key):
    # Decode Base64-encoded key
    encrypted_key = base64.b64decode(base64_encrypted_key)

    # Initialize AES cipher
    cipher = Cipher(algorithms.AES(decryption_key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the key
    decrypted_key = decryptor.update(encrypted_key) + decryptor.finalize()

    return decrypted_key

def main():
    # Prompt user to input the Base64-encoded encrypted key
    base64_encrypted_key = input("Enter the Base64-encoded encrypted key: ")

    # Prompt user to input the AES decryption key
    decryption_key = input("Enter the AES decryption key: ").encode()

    # Decrypt the key
    decrypted_key = decrypt_aes_key(base64_encrypted_key, decryption_key)

    print("Decrypted key:", decrypted_key)

if __name__ == "__main__":
    main()
