from aes import get_aes

CHUNK_SIZE = 1024

password = bytes(input('Password: '), encoding='UTF-8')
ecrypted_filename = input('Ecrypted file: ')
decrypted_filename = input('Desired decrypted filename: ')

aes_crypto = get_aes(password)

with open(ecrypted_filename, 'rb') as infile:
        with open(decrypted_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(aes_crypto.decrypt(chunk))