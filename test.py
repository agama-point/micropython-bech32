import bech32

btcaddr = bech32.encode("bc", 1, b"RANDOM BINARY DATA")
print(btcaddr)
print(bytes(bech32.decode("bc", btcaddr)[1]))

data=b"Some data to encode with bech32"
bits = bech32.convertbits(data, 8, 5)
bech32data = bech32.bech32_encode('lnurl', bits)

print(bits)
print(bech32data)

bech32decode = bech32.bech32_decode(bech32data)
origdata = bech32.convertbits(bech32decode[1], 5, 8, False)

print(bech32decode[1])
print(bytes(origdata))

print(bits == bech32decode[1])
print(data == bytes(origdata))
