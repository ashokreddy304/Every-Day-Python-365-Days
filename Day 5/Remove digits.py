def remove_digits(s):
    l = list(s)
    l1 = []
    for i in s:
        if not i.isdigit():
            l1.append(i)
    return "".join(l1)

s = input("Enter string: ")
print(remove_digits(s))