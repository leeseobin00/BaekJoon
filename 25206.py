# 등급에 따른 과목 평점을 dictionary로 만듬
# 입력받은 학점, 등급 값에서 등급을 과목 평점으로 변경
# 학점 X 과목 평점의 합을 구함
# 학점의 총합으로 나눔

grade_subject = {'A+':4.5, 'A0':4.0,
               'B+':3.5,'B0':3.0,
               'C+':2.5,'C0':2.0,
               'D+':1.5,'D0':1.0,
               'F':0.0,}

sum1 = 0.0
sum2 = 0.0

for i in range(20):
    title, score, grade = input().split()
    score = float(score)
    if grade != 'P':
        sum1 += score * grade_subject[grade]
        sum2 += score

print("%.6f" % (sum1 / sum2))