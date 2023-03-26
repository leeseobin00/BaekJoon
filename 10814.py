# n을 입력 받음
# for문을 통하여 n번 반복함
# list 내에 dictionary 형태로 값을 저장함

# age 비교를 통하여 값을 변경

def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i]['age'] > arr[i + 1]['age']:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap

n = int(input())
member = []

for i in range(n):
    age, name = input().split()
    member.append({'age': int(age), 'name': name})

bubble_sort(member)

for i in member:
    print(i['age'], i['name'])