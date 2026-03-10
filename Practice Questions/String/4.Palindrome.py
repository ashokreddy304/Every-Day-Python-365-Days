# Check whether a string is Palindrome.
def check_palindrome(s):
    if s == s[::-1]:
        return "given string is Palindrome"
    else:
        return "given string is not Palindrome"

s = input("Enter any string:")
s = s.strip().lower()
print(check_palindrome(s))

def reverse_string(s):
    l1 = []
    for i in range(-1,-(len(s)+1),-1):
        l = s[i]
        l1.append(l)
    return "".join(l1)
s = input("Enter any string:")
s = s.strip().lower()
print(reverse_string(s))