number = 0
var = 0
enter = int(input("Enter a number: "))

while number < enter:
    number = number + 1
    if number % 2 == 0:
        print(number, end = " ")
        var = var + number
print(f"\nSum of all even numbers is: {var}")
