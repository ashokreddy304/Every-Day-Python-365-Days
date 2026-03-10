def accessing(s):
    #Directly we can print
    print("Directly print:" ,s)
    #index
    print("Index: ",s[-1])
    #slicie 
    print("Slice: ",s[0:3])
    #while loop:
    print("===using while loop===")
    index = 0
    while index < len(s):
        print(s[index])
        index = index+1
    #for loop
    print("====using for loop ====")
    for i in s:
        print(i) 

s = input("Enter string ")
accessing(s)