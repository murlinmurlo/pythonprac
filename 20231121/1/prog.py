import sys

data = sys.stdin.buffer.read()
num_parts = data[0]
part_size = (len(data) - 1) // num_parts

if part_size == 0:
    part_size = 1
parts = [data[i * part_size:(i + 1) * part_size] for i in range(num_parts)]

sorted_parts = sorted(parts)

sorted_data = b''.join(sorted_parts)
sys.stdout.buffer.write(sorted_data)
