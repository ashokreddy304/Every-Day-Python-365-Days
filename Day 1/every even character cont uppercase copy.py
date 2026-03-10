def myfunc(s):
    l = list(s)
    for i in range(len(l)):
        if i%2==0:
            l[i] = l[i].upper()
    return "".join(l)

s = 'Ashok Reddy'
print(myfunc(s))