n1 = int(input())
n2 = int(input())

print(n1*(n2%10))
print(n1*int((n2/10)%10))
print(n1*int(n2/100))
print(n1*n2)