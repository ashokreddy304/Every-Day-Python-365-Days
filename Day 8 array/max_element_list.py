def fun(l):
    max = l[0]
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
    return max

def fun_v1(l):
    return max(l)

l = eval(input("Enter list: "))
result1 = fun(l)
result2 = fun_v1(l)
print(result1)
print(result2)