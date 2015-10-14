def prime(n):
    a = int(n ** 0.5)
    y = [2] + [i for i in range(2, a+1) if i % 2 == 1]

    if 1 < n < 10:
        if n in [2, 3, 5, 7]:
            return True
        else:
            return False
    else:
        test = []
        for i in y:
            d = n % i
            test += [d]
            if n % i == 0:
                return False
                break
        if 0 not in test:
            return True

n = int(input())
for number in range(0, n):
    print(prime(int(input())))
