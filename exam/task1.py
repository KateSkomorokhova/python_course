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
        x = " "
        return x

with open("answer.txt","a+") as out:
    for i in text:
        i = i.split()
        f = []
        for i in i:
            e = find_ka(i)
            f += [e]
        out.write(' '.join(f)+'\n')

a.close()



