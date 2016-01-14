import rsa
from rsa.bigfile import encrypt_bigfile, decrypt_bigfile

public_key, private_key = rsa.newkeys(2048)

with open('2048_rsa_key') as private_key_file:
    keydata = private_key_file.read()
pubkey = rsa.PrivateKey.load_pkcs1(keydata)

with open('input_aes.txt', 'rb') as infile, open('outputfile', 'wb') as outfile:
    encrypt_bigfile(infile, outfile, public_key)

with open('outputfile', 'rb') as infile, open('doutputfile', 'wb') as outfile:
    decrypt_bigfile(infile, outfile, private_key)
