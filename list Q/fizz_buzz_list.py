l = [1, 3, 5, 15, 7]
l1 = []
for i in l:
    if i%3 == 0 and i%5==0:
        l1.append("FizzBuzz")
    elif i % 3 == 0:
        l1.append('Fizz"')
    elif i%5 == 0:
        l1.append('Buzz')
    else:
        l1.append(i)

print(l1)