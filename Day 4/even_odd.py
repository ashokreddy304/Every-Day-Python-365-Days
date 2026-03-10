def even_odd_v1(n):
    return n%2==0

def even_odd_v2(n):
    return (n&1) == 0

def even_odd_v3(n):
    if n%2 == 0:
        return True
    else:
        return False

n = int(input("Enter any number: "))
print(even_odd_v1(n))
print(even_odd_v2(n))
print(even_odd_v3(n))
