def check_repeated(list_input):
    return len(list_input) == len(set(list_input))
list_input = [1,2,3,4]
# list_input = [1,2,2,3,4,4]
result = check_repeated(list_input)
print(result)
