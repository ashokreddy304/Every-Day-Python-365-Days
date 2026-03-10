def evn_odd(l):
    if len(l):
        return 0
    else:
        even = []
        odd = []
        for i in l:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return even,odd

l = eval(input("Enter list of elements: "))
even,odd = evn_odd(l)
print("Given list is {} and even elements is {}".format(l,even))
print("Given list is {} and odd elements is {}".format(l,odd))