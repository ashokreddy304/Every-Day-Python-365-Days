def sumofdigits_v1(n):
    sum = 0
    while n !=0:
        d = n%10
        sum = sum+d
        n = n//10
    return sum

n = int(input("Enter number: "))
print(sumofdigits_v1(n))