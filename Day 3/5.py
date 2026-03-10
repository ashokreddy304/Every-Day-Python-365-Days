def fun(n):
    c = 0
    i = 0
    while i<n:
        j = 0
        while j<n:
            c = c+1
            j = j+1
        i = i+1
    return c

print("N=100, number of instructions is O(N^2): ",fun(100))