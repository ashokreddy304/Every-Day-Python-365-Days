# def avg_list_v1(l):
#     sum = 0
#     for i in l:
#         sum = sum+i
#     return sum/len(l)

def avg_list_v2(l):
    if len(l) == 0:
        return 0.0
    else:
        sum = 0
        for i in l:
            sum = sum+i
        return sum/len(l)

#list = eval(input('Enter list of numbers: '))
list = []
result = avg_list_v2(list)
print(result)


