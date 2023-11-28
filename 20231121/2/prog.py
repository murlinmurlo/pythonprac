import sys

print(sys.stdin.buffer.read().decode().encode('latin1', errors='replace').decode('CP1251'))
