# Accept a number and display whether it is Prime
n = int(input("Enter a number: "))

for i in range(2, n//2 + 1):
    if n % i == 0:
        print("Not a prime number")
        break
else:
    print("", n, end=' is a Prime number')
# print(" is a prime number", n)
