def get_primes(numbers):
    primes = []
    for num in numbers:
        if num <2:
            continue

        is_prime = True
        for i in range(2,int(num*0.5)+1):
            if num%2==0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes

user_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(get_primes(user_input))