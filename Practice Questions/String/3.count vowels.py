# Write a program to count how many vowels exist in a string.
def count_vowels(s):
    l = ['a','e','i','o','u']
    count = 0
    for chr in s:
        if chr in l:
            count = count+1
    return count

s = input("Enter string: ")
s = s.strip().lower()
print(count_vowels(s))