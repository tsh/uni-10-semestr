import base64, os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def get_aes(password):
    # Password-Based Key Derivation hash-based message authentication code
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'pretend its random',
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return Fernet(key)

if __name__ == '__main__':
    DEFAULT_INPUT_FILENAME = 'input.txt'
    CHUNK_SIZE = 1024

    user_filename = input("File to encrypt (leave blank for use '{}'): ".format(DEFAULT_INPUT_FILENAME))
    input_filename = user_filename if user_filename else DEFAULT_INPUT_FILENAME

    ENCRYPTED_FILENAME = 'enc_{input_filename}'.format(input_filename=input_filename)
    DECRYPTED_FILENAME = 'dec_{input_filename}'.format(input_filename=input_filename)

    password = bytes(input('Password: '), encoding='UTF-8')

    aes_crypto = get_aes(password)

    # Encrypt
    with open(input_filename, 'rb') as infile:
        with open(ENCRYPTED_FILENAME, 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                        break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(aes_crypto.encrypt(chunk))

    # Decrypt
    with open(ENCRYPTED_FILENAME, 'rb') as infile:
            with open(DECRYPTED_FILENAME, 'wb') as outfile:
                while True:
                    chunk = infile.read(CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    outfile.write(aes_crypto.decrypt(chunk))