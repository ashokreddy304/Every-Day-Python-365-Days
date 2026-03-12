def fun(l):
    n = len(l)
    for i in range(0,n):
        count = 1
        for j in range(i+1,n):
            if l[i] == l[j]:
                count = count+1
        if count > n/2:
            return l[i]

l = [8,3,4,8,8]
print(fun(l))
