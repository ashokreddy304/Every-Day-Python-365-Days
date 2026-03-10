def fun_v1(a,b):
    return a if a>b else b 

def fun_v2(a,b):
    return max(a,b)

def fun_v3(a,b):
    if a>b:
        return a
    else:
        return b

def fun_v4(a,b):
    l = []
    l.append(a)
    l.append(b)
    return max(l)

def fun_v5(a,b):
    call = lambda a,b: a if a>b else b


a = int(input("Enter 1st number: "))
b = int(input("Enter 2cd number: "))

print("The vesrion_1",fun_v1(a,b))
print("The vesrion_2",fun_v2(a,b))
print("The vesrion_3",fun_v3(a,b))
print("The vesrion_4",fun_v4(a,b))
print("The vesrion_5",fun_v4(a,b))