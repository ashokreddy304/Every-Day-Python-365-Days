def fact_v1(n):
    fact = 1
    i = 1
    while i<=n:
        fact = fact * i
        i = i+1
    return fact

def fact_v2(n):
    if n ==0:
        return 1
    else:
        return n*fact_v2(n-1)

import math

def fact_v3(n):
    return math.factorial(n)

n = int(input("Enter number: "))

for i in range(1,n+1):
    print(i,fact_v1(i),fact_v2(i),fact_v3(i),sep="  ")