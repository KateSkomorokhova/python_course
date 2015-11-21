import sys
import re

data = sys.stdin.read()
results = re.findall("(Y|y)ou", data)
print(len(results))
