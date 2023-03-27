# input()으로 입력 받음
# string 자체를 list에 넣으면 하나씩 잘림
# sorted()를 사용한 다음 end=""로 출력

num = input()
num = list(num)
for i in sorted(num, reverse=True):
    print(i, end="")
