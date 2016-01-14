import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


INPUT_FILENAME = 'input.txt'
ENCRYPTED_FILENAME = 'encrypted_{input_filename}'.format(input_filename=INPUT_FILENAME)
DECRYPTED_FILENAME = 'decrypted_{input_filename}'.format(input_filename=INPUT_FILENAME)
CHUNK_SIZE = 1024

password = bytes(input('Password: '), encoding='UTF-8')
salt = os.urandom(16)
# Password-Based Key Derivation hash-based message authentication code
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
aes_crypto = Fernet(key)

# Encrypt
with open(INPUT_FILENAME, 'rb') as infile:
    with open(ENCRYPTED_FILENAME, 'wb') as outfile:
        while True:
            chunk = infile.read(CHUNK_SIZE)
            if len(chunk) == 0:
                    break
            else:
                outfile.write(aes_crypto.encrypt(chunk))

# Decrypt
with open(ENCRYPTED_FILENAME, 'rb') as infile:
        with open(DECRYPTED_FILENAME, 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(aes_crypto.decrypt(chunk))