# AES Encryption and Decryption Scripts

This repository contains two Python scripts for encrypting and decrypting data using the Advanced Encryption Standard (AES) algorithm.

## Requirements

- Python 3.x
- cryptography library (`pip install cryptography`)

## Encryption Script

### Usage
Run the following command to execute the encryption script:
```bash
python RandomBase64encodedAESgenerator.py

Description
Generates a random AES decryption key (256 bits).
Encrypts a sample key ("SecretKey123") using AES.
Base64-encodes the encrypted key.
Prints the generated AES decryption key and the base64-encoded encrypted key to the console.

Decryption Script

Usage
Run the following command to execute the decryption script:

bash
python base64AESdecryptor.py

Description

Prompts the user to input a base64-encoded encrypted key.
Prompts the user to input an AES decryption key.
Decrypts the input key using AES.
Prints the decrypted key to the console.

Note
Ensure that you have the required dependencies installed before running the scripts.

