# Accept 10 names and display the names whose length
# is greater than the average length
names = []
for i in range(1, 11):
    name = str(input("Enter a name: "))
    names.append(name)
length = [len(i) for i in names]
avg = sum(length)/10
greater = []
for n in names:
    if len(n) > avg:
        greater.append(n)
print(sorted(greater))
