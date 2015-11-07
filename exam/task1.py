a = open("yazkora.txt", "r")

text = a.read().replace("\n", " ").split(".")

def find_ka(x):
    tmp = []
    tmp += x
    z = len(tmp)-1
    s = tmp[z-1] + tmp[z]
    if s == "yo":
        return x
    else:
        x =" "
        return x

for i in text:
    i = i.split()
    f = []
    for i in i:
        e = find_ka(i)
        f += [e]
    print(" ".join(f))

