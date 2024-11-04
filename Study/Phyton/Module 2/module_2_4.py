numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
prime = []
NotPrime = []
for i in numbers:
    a = 0
    # -----------------------------------------------
    for j in numbers:
        if j>i:
            continue
        if i % j == 0 and j % j == 0 and j / 1 == j:
            a = a+1
    #-----------------------------------------------
    if a == 2:
        prime.append(i)
    if a > 2:
        NotPrime.append(i)
print(prime)
print(NotPrime)

