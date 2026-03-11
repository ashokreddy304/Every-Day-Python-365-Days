def fun(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i = i+1
    return True

l = [1,2,3,44,5,6]
print(fun(l))


def v2(l):
    l1 = sorted(l)
    return l == l1
l = [1,2,3,44,5,6]
print(v2(l))