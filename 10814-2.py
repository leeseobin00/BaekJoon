# n을 입력 받음
# for문을 통하여 n번 반복함
# list에 넣어 저장함

# age 비교를 통하여 값을 변경

def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if int(arr[i][0]) > int(arr[i + 1][0]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap

n = int(input())
member = []

for i in range(n):
    age, name = input().split()
    member.append((int(age), name))

bubble_sort(member)

for i in member:
    print(i[0], i[1])