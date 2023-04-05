# 문자열을 입력받음
# [:10]만큼을 출력
# [10::]를 새로운 str로 저장
import sys
input = sys.stdin.readline

str = input()

for i in range(int(len(str) / 10)):
    print(str[:10])
    str = str[10::]
# 틀림
