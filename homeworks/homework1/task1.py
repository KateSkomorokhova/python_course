word = input()
num = int(input())

if word == 'утюг':
    if num == 1 or num % 10 == 1 and num % 100 != 11:            # 1. 21. 31 101. 121 иксл11,111 и тд.
        print(num, word)
    elif 10 > num % 10 > 4 or num % 10 == 0 or 10 < num % 100 < 20:      # 5-9   10.20.30.100.  12-19
        print(num, word + 'ов')
    else:                                        # 2-4 b ит.д. искл 12-19
        print(num, word + 'а')
else:
    if num == 1 or num % 10 == 1 and num % 100 != 11:
        print(num, 'ложка')
    elif 10 > num % 10 > 4 or num % 10 == 0 or 10 < num % 100 < 20:
        print(num, 'ложек')
    else:
        print(num, 'ложки')