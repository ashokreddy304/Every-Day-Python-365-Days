def fun_v1(l):
    sum = 0
    for i in l:
        sum = sum+i
    return sum

def fun_v2(l):
    return sum(l)

import functools
def fun_v3(l):
    return functools.reduce(lambda i,j:i+j,l)

l = [1,2,3,4]
print(fun_v1(l))
print(fun_v2(l))
print(fun_v3(l))