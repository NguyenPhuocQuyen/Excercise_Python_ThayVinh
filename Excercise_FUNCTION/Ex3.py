def calculate_list():
    number_list =[]
    number = int(input("Please enter a value list: "))
    for i in range(number):
        element = float((input("Enter a value element: ")))
        number_list.append(element)
        average = sum(number_list)/len(number_list)
    return f'Average of list = {average}'
print(calculate_list())
