# 3개의 숫자 입력을 받음
# 만약 b가 c보다 크면 -1 출력
# c - b 의 차이 * n이 a를 넘는 수를 찾아라
# => a / (c-b) + 1 을 출력
num = list(map(int, input().split()))

# b와 c가 같을 때도 손익분기점이 존재하지 않는다.
# 분모인 b-c가 0이 되므로 => X
if num[1] >= num[2]:
    print(-1)
else:
    print(int(num[0] / (num[2]-num[1]))+1)
