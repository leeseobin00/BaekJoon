word = input().upper()
list = list(word)
max_num = 0
alphabet = [0] * 26

for i in list:
    alphabet[ord(i)-65] += 1

for i in alphabet:
    if max(alphabet) == i:
        max_num += 1

if max_num == 1:
    print(chr(alphabet.index(max(alphabet))+65))
else:
    print("?")
