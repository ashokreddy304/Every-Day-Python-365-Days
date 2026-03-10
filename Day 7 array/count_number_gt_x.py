def count_x_val_gt(l,x):
    count = 0
    for i in l:
        if x > i:
            count = count+1
    return count

l = eval(input('enter list of numbers: '))
x = int(input("Enter number to check count: "))
result = count_x_val_gt(l,x)
print(result)
