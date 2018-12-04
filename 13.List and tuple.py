# Accept a list of numbers and display the number
# and its corresponding square in a tuple
num = []
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    else:
        num.append(n)
tup = ()
for i in num:
    tup = i, i*i
    print(tup)

