import struct  

# Two little-endian unsigned 32-bit integers: 1 and 42.
payload = b"\x01\x00\x00\x00\x2a\x00\x00\x00"

a, b = struct.unpack("<II", payload)
print(f"[decoder] Decoded values: {a}, {b}")
print(f"[decoder] Using struct from: {struct.__file__}")
