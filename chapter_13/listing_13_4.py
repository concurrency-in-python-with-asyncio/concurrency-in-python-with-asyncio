import sys

[sys.stdout.buffer.write(b'Hello there!!\n') for _ in range(1000000)]

sys.stdout.flush()
