t = int(input())

result_str = []

for i in range(t):
    str = input()
    result_str.append(str[0]+str[len(str)-1])

for i in result_str:
    print(i)