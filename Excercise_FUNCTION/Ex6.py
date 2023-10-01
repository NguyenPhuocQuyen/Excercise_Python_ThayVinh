def calculate(base, exponent):
    power = base ** exponent
    return power
base = int(input("Please enter a base number: "))
exponent = int(input("Please enter a exponent number: "))
result = calculate(base, exponent)
print(f"Power of {base} and {exponent} is: {result}")