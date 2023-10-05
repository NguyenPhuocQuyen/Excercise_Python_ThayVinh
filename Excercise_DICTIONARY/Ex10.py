dict_list_1 = {
    'name': 'Quyen',
    'class': '20CDT2',
    'student ID' : '101200284',
    'address': 'Quang Nam'
}

dict_list_2 = {
    'name': 'Hung',
    'class': '20CDT',
    'student ID' : '101200212',
    'telephone':'123123123'
}

list_key = []
for key in dict_list_2:
    if key in dict_list_1:
        list_key.append(key)
print(list_key)

