def minOf3_v1(a,b,c):
    return min(a,b,c)

def minOf3_v2(a,b,c):
    return a if a<b and a<c else b if b<c else c

def minOf_v3(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c

def minOf_v4(a,b,c):
    call = lambda a,b,c : a if a<b and a<c else b if b<c else c
    return call(a,b,c)


a = int(input("Enter 1st number: "))
b = int(input("Enter 2cd number: "))
c = int(input("Enter 3rd number: "))

print("V1: ",minOf3_v1(a,b,c))
print("V2: ",minOf3_v2(a,b,c))
print("V3: ",minOf_v3(a,b,c))
print("V4: ",minOf_v3(a,b,c))