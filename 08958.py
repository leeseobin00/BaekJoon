# string을 입력받음
# 처음에 점수는 1
# 만약 o이면 결과 점수 +1, 점수 +1
# 만약 x이면 점수 = 1로 설정
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    quiz = list(input())
    score = 1
    result_score = 0
    for j in quiz:
        if j == 'O':
            result_score += score
            score += 1
        else:
            score = 1
    print(result_score)
