# input = [10,40,30,20]
# output = [20,10,40,30]
#======== v_1 ===========
l  = [10,40,30,20]
print(l[-1:-2:-1]+l[0:len(l)-1])

# ========== v_2 ============
l  = [10,40,30,20]
l.insert(0,l.pop(-1))
print(l)

# ========= v_3 =============
def rightrotation(l):
    n = len(l)
    x = l[n-1]
    for i in range(n-1,0,-1):
        l[i] = l[i-1]
    l[0] = x 

l  = [10,40,30,20]
print(l)
rightrotation(l)
print(l)