text = list(input().upper())
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

total = 0

for x in text:
    for y in dial:
        if x in y:
            total += (dial.index(y) + 2 + 1)
print(total)
