# cách 1
# string = str(input('Please enter a string: '))
# string_suffix = str(input('Please enter a string suffix: '))

# if string.endswith(string_suffix):
#     print('True')
# else:
#     print('False')


#Cách 2
string = str(input("Please enter a string: "))
string_prefix = str(input("Please enter a prefix: "))

if len(string_prefix) > len(string):
    print("No Suitable")
else: 
    check = True
    for char in range(1,len(string_prefix)):
        print(char)
        if string[-char] != string_prefix[-char]:
            check = False
            break
    if check:
        print("True")   
    else:
        print("False")