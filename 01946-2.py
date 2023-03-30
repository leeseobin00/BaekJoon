import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    count = 1
    score = []

    n = int(input())

    for j in range(n):
        doc, inter = map(int, input().split())
        score.append((doc, inter))

    score.sort()
    min_inter = score[0][1]  # 1차 서류심사를 통과한 지원자들 중에서 면접시험 성적이 가장 좋은 지원자의 성적을 기록합니다.
    for j in range(1, n):
        if score[j][1] < min_inter:
            count += 1
            min_inter = score[j][1]  # 면접시험 성적이 가장 좋은 지원자의 성적을 갱신합니다.

    print(count)