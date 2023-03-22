c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    #n = list[0]
    #mean = (sum(list)-list[0])/list[0]
    mean = sum(scores[1:])/scores[0]
    count = 0
    for j in range(1, len(scores)):
       if scores[j] > mean:
           count += 1
    # print("{:.3f}%".format(count/(len(list)-1)*100))
    result = round(count/scores[0]*100, 3)
    print(f"{result:.3f}%")