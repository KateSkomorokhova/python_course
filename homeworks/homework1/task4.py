text = input()
text_letter = set(text)
count_letter = {}
for letter in text_letter:
    value = text.count(letter)
    count_letter[letter] = value

regularize = list(count_letter.keys())
regularize.sort()

for i in regularize:
    print(i, count_letter[i])
