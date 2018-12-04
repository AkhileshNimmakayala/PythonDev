# Accept a string and display each character
# and its corresponding ASCII code
string = str(input("Enter a string: "))
for each in string:
    t = (each, ord(each))
    print(t)
