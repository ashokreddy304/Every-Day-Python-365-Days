l = [1,2,3,4,5,6]
print(l)
l1 = l[1:] + l[0:1]
print(l1)


l3 = [1,2,3,4,5]
l3.append(l3.pop(0))
print(l3)


def leftRoateByone(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x
    return l
l3 = [1,2,3,4,5]
print(leftRoateByone(l3))