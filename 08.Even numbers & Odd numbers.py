# Accept 10 numbers from user and display all evens
# in one list and odds in another
numbers = []
for i in range(1, 11):
    num = int(input("Enter a number: "))
    numbers.append(num)
even = []
odd = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(even, odd, sep='\n')
