import re
import sys

data = sys.stdin.readlines()
for index, line in enumerate(data):
    if re.findall("^ *(\w+\.)+\w+ = ", line):
        bgg = re.findall("^ *(.+) = ", line)
        print(index + 1, bgg[0])
    elif re.findall("^ *\w+ = ", line):
        bgg = re.findall("^ *(\w+) = ", line)
        print(index + 1, bgg[0])
    elif re.findall("^ *[\w+, ]+\w+ = ", line):
        bgg = re.findall("^ *([\w+, ]+\w+) = ", line)
        for i in bgg:
            w = re.findall("[a-zA-Z_]+", i)
            print(index + 1, end=" ")
            for i in w:
                print(i, end=" ")
            print()
