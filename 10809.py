s = input()

alphabet = [-1] * 26
list = list(s)

for i in list:
    alphabet[ord(i)-97] = list.index(i)

print(*alphabet)