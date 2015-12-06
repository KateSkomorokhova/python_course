import re
import sys

data = sys.stdin.readlines()
for line in data:
    words = (re.findall('[a-zA-Z0-9]+', line))
    print(" ".join(words), end=" ")
