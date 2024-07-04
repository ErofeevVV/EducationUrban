numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = numbers
not_prime = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0:
            not_prime.append(i)
            break
for i in not_prime:
    for j in numbers:
        if i == j:
            prime.remove(i)
prime.remove(1)
print(f'Primes  {prime}')
print(f'Not Primes {not_prime}')