list_dict = {
    'name': 'Quyen',
    'class': '20CDT2',
    'address': 'Quang Nam'
}
before = dict(list_dict.items())
print(f'List_dict before remove: {before}')
key_remove = input('Please enter a key to remove: ')
if key_remove in list_dict:
    del list_dict[key_remove]
    print('List_dict after remove',list_dict)
else: 
    print(f'Key {key_remove} does not exist')