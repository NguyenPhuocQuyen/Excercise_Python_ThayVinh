string = str(input('Please enter a string: '))
string_list = string.split(' ')
element = input('Please enter a element to join: ')

string_new = element.join(string_list)
print(f'String_new is: {string_new}')