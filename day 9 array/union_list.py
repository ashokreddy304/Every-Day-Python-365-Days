l1 = [1,2,3,4,5]
l2 = [2,4,5,6,7]

l = []
for i in l1:
    if i in l2:
        l.append(i)
print(l)