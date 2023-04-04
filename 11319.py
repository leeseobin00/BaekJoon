# 문자열에서 공백 제거
# 모음을 배열에 저장
# 문자열 for문으로 돌면서 모음 배열에 들어가는 갯수 계산

import sys
input = sys.stdin.readline

vowels = ['A','E','I','O','U','a','e','i','o','u']

t = int(input())

for i in range(t):
    str = input()
    str = str.replace(" ", "")
    vowel = 0
    for j in str:
        if j in vowels:
            vowel += 1
    print(len(str)-vowel-1, vowel)
