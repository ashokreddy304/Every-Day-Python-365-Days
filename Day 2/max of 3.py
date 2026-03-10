def maxOfThree_v1(a,b,c):
    return max(a,b,c)

def maxOfThree_v2(a,b,c):
    return a if a>b and a>c else b if b>c else c

def maxOfThree_v3(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

def maxOfThree_v4(a,b,c):
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    return max(l)

def maxOfThree_v5(a,b,c):
    call  = lambda a,b,c : a if a>b and a>c else b if b>c else c
    return call(a,b,c)



a = int(input("Enter 1st number: "))
b = int(input("Enter 2cd number: "))
c = int(input("Enter 3rd number: "))

print("vesrion v1:",maxOfThree_v1(a,b,c))
print("Vesrion v2:",maxOfThree_v2(a,b,c))
print("Vesrion v3:",maxOfThree_v3(a,b,c))
print("Vesrion v4:",maxOfThree_v4(a,b,c))
print("Vesrion v5:",maxOfThree_v5(a,b,c))