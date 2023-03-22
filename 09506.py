factor = []

while True:
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            factor.append(i)

    if sum(factor) == n:
        # print(str(n) + " = " + str(factor[0]), end=" ")
        # for i in factor[1:]:
        #     print(" + " + str(i), end= "")
        print(n, " = ", " + ".join(str(i) for i in factor), sep="")
    else:
        print(str(n) + " is NOT perfect.")
    factor.clear()
