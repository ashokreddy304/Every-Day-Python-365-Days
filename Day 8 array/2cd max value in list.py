def fun(l):
    max = 0
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
    return max

def fun_2cd_max(l):
    max= fun(l)
    smax = None
    for i in l:
        if i != max:
            if smax == None:
                smax = i
            else:
                smax = smax if smax > i else i
    return smax

l = eval(input("Enter list: "))
result1 = fun_2cd_max(l)
print(result1)


#vesrion:
#========
l = [1,2,33,4,5,6]
l.sort()
print(l[-2])