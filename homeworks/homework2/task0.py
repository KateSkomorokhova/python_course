def plural(num, work_word):
    n = num % 10
    n1 = num % 100
    if num == 1 or n == 1 and n1 != 11:
        return num, work_word[0]
    elif 10 > n > 4 or n == 0 or 10 < n1 < 20:
        return num, work_word[1]
    else:
        return num, work_word[2]

words_iron = ['утюг', 'утюгов', 'утюга']
words_spoon = ['ложка', 'ложек', 'ложки']
words_accordion = ['гармошка', 'гармошек', 'гармошки']
word_teapot = ['чайник', 'чайников', 'чайника']
word = input()
num = int(input())

if word in words_iron:
    work_word = words_iron
elif word in words_spoon:
    work_word = words_spoon
elif word in words_accordion:
    work_word = words_accordion
else:
    work_word = word_teapot

print(' '.join(map(str, plural(num, work_word))))