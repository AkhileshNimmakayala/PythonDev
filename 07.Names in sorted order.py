# Accept names from user until End is entered
# and display names in sorted order
names = []
while True:
    name = input("Enter a name: ")
    if name == "end":
        break
    names.append(name)
for n in sorted(names):
    print(n)
