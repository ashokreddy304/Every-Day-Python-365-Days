def swaping2numbers(n1,n2):
    print(f"before swaping: n1={n1} and n2={n2}")
    n1,n2 = n2,n1
    print(f"after swaping: n1={n1} and n2={n2}")

n1 = int(input("Enter any number: "))
n2 = int(input("Enter any number: "))
print(swaping2numbers(n1,n2))