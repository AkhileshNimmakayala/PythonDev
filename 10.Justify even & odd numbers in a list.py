# Accept 10 numbers and display all even numbers in the
# right corner and odd numbers in the left corner of a list
numbers = []
for i in range(1, 5):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        numbers.append(num)
    else:
        numbers.insert(0, num)
print('\n', numbers)
