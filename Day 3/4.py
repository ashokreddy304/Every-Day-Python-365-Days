def myfunc(n,digit):
    flag = False
    while n != 0:
        d = n%10
        if digit == d:
            flag = True
            break
        n = n//10
    return flag

n = int(input("Enter number: "))
digit = int(input("Enter digit: "))
print(myfunc(n,digit))