def isprime1(n):
	factors=0
	for i in range(1,n+1):
		if n%i==0:
			factors=factors+1
	return factors==2

n = int(input("Enter number: "))
print(isprime1(n))
