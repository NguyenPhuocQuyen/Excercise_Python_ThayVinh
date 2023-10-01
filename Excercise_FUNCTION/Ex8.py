def calculate_product(*args):
    var = 1
    for element in args:
        var = var * element 
    return var
result = calculate_product(1,2,3,4,5)
print(f'Prodcut = {result}')