data = [int(i) for i in input().split()]
uneven = data[0::2]
uneven.sort()
even = data[1::2]
even.sort()
even.reverse()

i = 0
new_data = []
count = len(even)
while i < count:
    new_data += [uneven[i], even[i]]
    i += 1
print(' '.join([str(i) for i in new_data]))
