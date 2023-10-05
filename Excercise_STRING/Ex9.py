#Cách 1
# string = str(input("Please enter a string: "))
# string_prefix = str(input("Please enter a prefix: "))
# if string.startswith(string_prefix):
#     print("True")
# else:
#     print("False")

#Cách 2
string = str(input("Please enter a string: "))
string_prefix = str(input("Please enter a prefix: "))

if len(string_prefix) > len(string):
    print("No Suitable")
else: 
    check = True
    for char in range(len(string_prefix)):
        print(char)
        if string[char] != string_prefix[char]:
            check = False
            break
    if check:
        print("True")   
    else:
        print("False")