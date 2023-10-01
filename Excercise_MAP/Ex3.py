def convert(string):
    return int(string)
string = ['123', '456', '789']
result = list(map(convert, string))
print(result)