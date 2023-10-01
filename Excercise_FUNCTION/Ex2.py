def check(number):
    if number % 2 ==0:
        return (f'Number {number} is a even')
    else:
        return (f'Number {number} is not a even')
number = int(input("Please a number to check: "))
check_number = check(number)
print(check(number))
    