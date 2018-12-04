numbers = set()
primes = set()
for i in range(50, 101):
    if i % 2 != 0:
        numbers.add(i)
print(numbers)
for n in numbers:
    for i in range(2, n//2 + 1):
        if n % i == 0:
            break
    else:
        primes.add(n)
print(sorted(primes))
print(sorted(numbers - primes))
# Sets are unsorted and therefore calling sorted returns list
