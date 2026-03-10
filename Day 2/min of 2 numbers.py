def minOfTwo_v1(a,b):
    return f"The 1st number is {a} and 2cd number is {b} and the min number is {min(a,b)}"

def minOfTwo_v2(a,b):
    if a<b:
        return f"The numbers are {a} and {b} min nuber is {a} "
    else:
        return b
    
def minOfTwo_v3(a,b):
    l = []
    l.append(a)
    l.append(b)
    return min(l)

def minOfTwo_v4(a,b):
    return a if a<b else b

def minOfTwo_v5(a,b):
    call = lambda a,b : a if a<b else b
    return call(a,b)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2cd number: "))
print("The vesrion_v1:",minOfTwo_v1(a,b))
print("The vesrion_v2:",minOfTwo_v2(a,b))
print("The vesrion_v3:",minOfTwo_v3(a,b))
print("The vesrion_v4:",minOfTwo_v4(a,b))
print("The vesrion_v5:",minOfTwo_v5(a,b))