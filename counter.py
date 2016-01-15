import math


def byte2bits(bytes):
    for b in bytes:
        for i in range(8):
            yield (b >> i) & 1


def bits4file(filename):
    bits_arr = []
    f = open(filename, 'rb')
    try:
        byte = f.read(1)
        while byte != b'':
            bt = list(byte2bits(byte))
            bits_arr.append(bt)
            byte = f.read(1)
    finally:
        f.close()
    return bits_arr


def count_fq(bits_arrs):
    fq = {}
    for bit_arr in bits_arrs:
        for i, bit in enumerate(bit_arr):
            try:
                fq[(i, bit)] += 1
            except KeyError:
                fq[(i, bit)] = 0
    return fq


def count_percent(fq, total):
    result = {}
    for position in range(8):
        for bit in (0, 1):
            try:
                result[(position, bit)] = round(fq[(position, bit)] / total * 100, 3)
            except KeyError:
                result[(position, bit)] = 0
    return result


orig_bits = bits4file('input.txt')
orig_fq = count_fq(orig_bits)
total_vals_orig = sum(orig_fq.values())
percent_orig = count_percent(orig_fq, total_vals_orig)

enc_bits = bits4file('enc_input.txt')
enc_fq = count_fq(enc_bits)
total_vals_enc = sum(enc_fq.values())
percent_enc = count_percent(enc_fq, total_vals_enc)


print('Pos\tBit\tInput\tEncrypted')
for position in range(8):
    for bit in (0, 1):
        pass
