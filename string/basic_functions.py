def basic_functions(s):
    print("=== print Entire String ===")
    print(s)
    print("===len of string ===")
    print(len(s))
    print("=== Max of Character ===")
    print(max(s))
    print("=== Min of Character ===")
    print(min(s))
    print("=== Sorted string ===")
    print(sorted(s))
    print("=== sorted with reverse ===")
    print(sorted(s,reverse=True))

#s = input("Enter any string: ")
s = "hello"
basic_functions(s)