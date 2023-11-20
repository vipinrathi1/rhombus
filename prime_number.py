def prime_checker(number):
    is_prime = True
    for i in range(2, round(n/2)):
        if n % i == 0:
            is_prime = False
    if is_prime is True:
        print(f"{n} is a prime number ")
    else:
        print(f"{n} is not a prime number ")

n = int(input("Enter the number: "))
prime_checker(number=n)





