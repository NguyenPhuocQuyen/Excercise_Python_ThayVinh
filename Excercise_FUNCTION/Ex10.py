def find_odd_number(*args):
    odd_number = []
    for element in args:
        if element % 2 != 0:
            odd_number.append(element)
    return odd_number
result = find_odd_number(1,2,3,4,5,6,7,8,9,10,11,12)
print(result)