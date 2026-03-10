def positive_negative(s):
    i1 = 0
    i2 = -len(s)
    while i1<len(s):
        print(f"+ve index {i1} value {s[i1]} and -ve index {i2} value {s[i2]}")
        i1 = i1+1
        i2 = i2+1

s = input("Enter string: ")
s1 = s.lower().strip()
positive_negative(s1)
