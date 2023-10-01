def convert(Celsius): 
    return (Celsius * 9/5)+32
Celsius = [15, 25, 35, 45, 55]
result = list(map(convert, Celsius))
print(f'Convert to Fahrenhrit: {result}')