# cách 1
# string = str(input('Please enter a string: '))
# string_suffix = str(input('Please enter a string suffix: '))

# if string.endswith(string_suffix):
#     print('True')
# else:
#     print('False')


#Cách 2
string = str(input("Please enter a string: "))
string_suffix = str(input("Please enter a suffix: "))

if len(string_suffix) > len(string):
    print("No Suitable")
else: 
    check = True
    for char in range(1,len(string_suffix)):
        print(char)
        if string[-char] != string_suffix[-char]:
            check = False
            break
    if check:
        print("True")   
    else:
        print("False")