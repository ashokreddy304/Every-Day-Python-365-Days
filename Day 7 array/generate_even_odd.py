even = []
odd = []
for i in range(0,11):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

def even_odd(x,y):
    even = [i for i in range(x,y+1) if i%2==0 ]
    odd =  [i for i in range(x,y+1) if i%2!=0 ]
    return even,odd

even,odd = even_odd(1,10)
print(even)
print(odd)