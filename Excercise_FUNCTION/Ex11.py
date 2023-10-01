def calculate_percentage(total_value, *value):
    number_list = []
    if total_value == 0: 
        return 'No valid'
    for element in value:
        element = element/total_value
        number_list.append(element)
    return number_list
total_value = 1000
value = 200,500,300
result = calculate_percentage(total_value, *value)
print(result)
    
