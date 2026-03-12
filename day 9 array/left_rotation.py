def leftRotationNumofDigt(l,d):
    return l[d:] + l[:d]

l = eval(input("Enter list: "))
d = int(input("Enter number of rotation: "))
print(leftRotationNumofDigt(l,d))
# =================== V_2 ======================================
def leftRotationNumofDigt(l,d):
    for  i in range(0,d):
        l.append(l.pop(0))
        

l = [1,2,3,4,5,6]
d = 2
leftRotationNumofDigt(l,d)
print(l)