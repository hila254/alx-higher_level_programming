#!/usr/bin/python3
# 100-print_tebahpla.py

"""Print the ASCII alphabet in reverse order alternating between lowercase and uppercase, without a new line."""

for c in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(c)), end="")
