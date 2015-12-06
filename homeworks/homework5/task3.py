import re
import sys
data = sys.stdin.readlines()
count = 0
for line in data:
    if re.findall("\w+ = ", line):
        bgg = re.findall("(\w+) = ",line)
        count += 1
        print(count, bgg[0])
    else:
        count += 1
