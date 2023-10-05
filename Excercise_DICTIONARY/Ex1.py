#Cách 1
# dict_information = {
#     'name': 'Quyen',
#     'class': '20CDT2'
# }
# dict_information['address'] = 'QuangNam'
# print(dict_information)

#Cách 2
dict_information = {
    'name': 'Quyen',
    'class': '20CDT2'
}
key = str(input('Please enter key:'))
value = str(input('Please enter value:'))
dict_information[key] = value
print(dict_information)