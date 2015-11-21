import re
import math

with open("dict.txt") as words:
    word_yo = 0
    word_ka = 0
    word_rest = 0
    for line in words:
        if re.findall("\w+yo", line) != []:
            word_yo += 1
        elif re.findall("\w+ka", line) != []:
            word_ka += 1
        else:
            word_rest += 1

if word_yo < 7:
    k = word_yo
else:
    k = 7

var_yo = 0
for i in range(0, k):
    var_yo += math.factorial(word_yo)//math.factorial(i)
sentence = var_yo * word_ka * word_rest
print(sentence)