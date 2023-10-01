prime = lambda number: number > 1 and all(number % i != 0 for i in range(2,number))
numbers = [4,5,6,7,8,9,10,11,12]

result = list(map(prime, numbers))
print(result)