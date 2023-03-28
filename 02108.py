n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
arr.sort()

print('1f'%sum(arr)/len(arr))
print(arr[int(n/2)+1])