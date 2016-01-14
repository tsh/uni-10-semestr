import pyaes
import hashlib

# Any mode of operation can be used; for this example CTR
inp = input('Password: ')
key = bytes(hashlib.sha1(bytes(inp, encoding='UTF-8')).hexdigest()[0:32], encoding='UTF-8')

# Create the mode of operation to encrypt with
mode = pyaes.AESModeOfOperationCTR(key)

# The input and output files
file_in = open('out.txt')
file_out = open('decs.txt', 'wb')

# Encrypt the data as a stream, the file is read in 8kb chunks, be default
pyaes.decrypt_stream(mode, file_in, file_out)

# Close the files
file_in.close()
file_out.close()