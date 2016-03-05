my_class = [A, B, C]
parent = []

for i in my_class:
    if issubclass(D, i) == True:
        parent.append(str(i)[-3])

print(" ".join(parent))
