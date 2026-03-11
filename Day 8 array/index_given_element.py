def func(l,x):
    for i in range(len(l)):
        if x == l[i]:
            return i
    return None

l = eval(input("Enter list of element: "))
x = int(input("Enter value: "))
#l = [1,2,3,4,5]
#x = 3
result = func(l,x)
print(result)