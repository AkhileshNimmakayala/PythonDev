# Accept 10 numbers and display the average
total = 0
for i in range(1, 10+1):
    n = int(input("Enter a number: "))
    total += n
Average = total//10
print("Average of numbers is ", Average)
