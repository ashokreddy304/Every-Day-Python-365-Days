def reverse_num(n):
    while n != 0:
        d = n%10
        print(d)
        n=n//10
    



n = int(input("enter number"))
print(reverse_num(n))