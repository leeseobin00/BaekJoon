# 먼저 테스트 케이스를 입력 받음
# for문을 통해서 테스트 케이스만큼 반복문을 돌릴 것이다

# n을 입력 받고 for문을 통해서 n만큼 테스트 케이스를 돌릴 것이다.

# 먼저 A에서 1등인 사람 찾기
# 다른 사람들은 A에서 1등한 사람보다 B의 등수가 높아야함
# 높은 사람들만 다른 배열에 저장
# B과목에서 가장 등수가 높은 사람
# 그 사람보다 A 등수가 더 높아야함
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    count = 1
    score = []
    new_score = []

    n = int(input())

    for j in range(n):
        doc, inter = map(int, input().split())
        score.append((doc, inter))

    score.sort(key=lambda x: x[0])
    new_score.append(score[0])
    print(new_score)
    for j in range(1, n):
        if score[j][1] < score[0][1]:
            count += 1
            new_score.append(score[j])
    print(count)
    print(new_score)
    new_score.sort(key=lambda x: x[1])
    print(new_score)
    for j in range(1, len(new_score)):
        print(new_score[j], new_score[0])
        if new_score[j][0] > new_score[0][0]:
            count -= 1

    print(count)