# Accept 10 names and display the
# largest in terms of characters and length
names = []
for i in range(0, 4):
    name = str(input("Enter a name: "))
    names.append(name)
print(names)
largestchr = []
for i in names:
    if i > max(largestchr, default='A'):
        largestchr.append(i)
    else:
        largestchr.insert(0, i)
print(largestchr)
print("Largest name by character is ", max(largestchr))

nameslen = [len(i) for i in names]
largestlen = []
for i in names:
    if len(i) > max(nameslen):
        largestlen.append(i)
    else:
        largestlen.insert(0, i)
print(largestlen)
print("Largest name by length is ", max(largestlen, key= len(largestlen)))
