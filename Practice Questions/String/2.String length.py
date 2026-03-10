# Write a program to find the length of a string without using len().

def str_len(s):
    count = 0
    for chr in s:
        count = count+1
    return count

s = input("Enter string: ")
print(str_len(s))