#cách 1
# list_dict = {
#     'name': 'Quyen',
#     'class': '20CDT2',
#     'address': 'Quang Nam'
# }
# list_key = list_dict.keys()
# print(list_key)
# check_key = input('Please enter key to check: ')
# check = True
# for key in list_key:
#     if key != check_key:
#         check = False
#         break 
# if check:
#     print('Key exists')
# else:
#     print('Key does not exist')

#Cách 2
list_dict = {
    'name': 'Quyen',
    'class': '20CDT2',
    'address': 'Quang Nam'
}
check_key = input('Please enter key to check: ')
if check_key in list_dict:
    print('Key exists')
else: 
    print('Key does not exist')