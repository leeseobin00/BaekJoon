n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print("Case #" + str(i+1) + ": " + str(a) + " + " + str(b) +" = "+ str(a+b))
    