def rightrorate(l,d):
    for i in range(0,d):
        l.insert(0,l.pop(-1))

l = [1,2,3,4,5]
d = int(input("Enter number of rotation: "))
rightrorate(l,d)
print(l)