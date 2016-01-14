import rsa
from rsa.bigfile import encrypt_bigfile, decrypt_bigfile

public_key, private_key = rsa.newkeys(2048)


with open('input.txt', 'rb') as infile, open('rsa_crypted', 'wb') as outfile:
    encrypt_bigfile(infile, outfile, public_key)

with open('rsa_crypted', 'rb') as infile, open('decrypted.txt', 'wb') as outfile:
    decrypt_bigfile(infile, outfile, private_key)
