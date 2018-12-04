names = set()
while True:
    name = str(input("Enter a name: "))
    if name == 'end':
        break
    names.add(name.upper())
print(sorted(names))
