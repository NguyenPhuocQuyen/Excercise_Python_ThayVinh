string = str(input("Please enter a string: "))
characters_check = input("Please enter characters to check: ")
var = 0
for character in string:
    if character == characters_check:
        var += 1
print(f"The occurrence of characters is: {var}")