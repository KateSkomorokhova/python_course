def euclid(a, b):
    def nod(a, b):
        residue = a % b
        if residue != 0:
            a = b
            b = residue
            return nod(a, b)
        else:
            return b

    if a > b:
        if a % b == 0:
            return b
        else:
            return nod(a, b)

    else:
        if b % a == 0:
            return a
        else:
            return nod(b, a)

a, b = [int(i) for i in input().split()]
print(euclid(a, b))

