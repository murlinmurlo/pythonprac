import struct
s = struct.pack("bhl", 3, 0x432, 0x234234)
print(list(s))
