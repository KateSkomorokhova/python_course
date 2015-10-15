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


def rpfilter(a, *args):
    s = []
    for arg in args:
        nod = euclid(a, arg)
        if nod == 1:
            s.append(arg)
    return s

a = [int(i) for i in input().split()]
a1 = a[0]
if len(a) == 1:
    print('None')
else:
    a2 = a[1:]
    list_result_num = rpfilter(a1, *a2)
    if len(list_result_num) == 0:
        print('None')
    else:
        print(' '.join(map(str, list_result_num)))

