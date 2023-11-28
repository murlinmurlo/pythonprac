import sys
import struct

try:
    wav = sys.stdin.buffer.read()
    if len(wav) < 44 or struct.unpack("4s", wav[8:12])[0] != b"WAVE":
        print("NO")
    else:
        size = struct.unpack('i', wav[4:8])[0]
        audio_type = struct.unpack('h', wav[20:22])[0]
        channels = struct.unpack('h', wav[22:24])[0]
        rate = struct.unpack('i', wav[24:28])[0]
        bits = struct.unpack('h', wav[34:36])[0]
        data_size = struct.unpack('i', wav[40:44])[0]
        print(f"Size={size}, Type={audio_type}, Channels={channels}, Rate={rate}, Bits={bits}, Data size={data_size}")
except struct.error:
    print("NO")