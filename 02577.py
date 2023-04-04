# 곱한 결과 값
# 배열을 0-9번째 index까지 0으로 초기화
# 배열에 각각의 값이 얼마나 쓰였는지 저장
# for문을 결과의 길이만큼 실행함
# 각각의 자리수에 해당하는 배열의 index에 +1
a = int(input())
b = int(input())
c = int(input())

arr = [0 for i in range(10)]

result = list(str(a*b*c))

for i in result:
    arr[int(i)] += 1

for i in arr:
    print(i)