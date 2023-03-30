T = int(input())

for i in range(T):
    C = int(input())
    c_list = []
    c_list.append(int(C / 25))
    C = C % 25
    c_list.append(int(C / 10))
    C = C % 10
    c_list.append(int(C / 5))
    c_list.append(C % 5)

    print(*c_list)