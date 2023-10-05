# number = int(input("Nhập một số dương: "))
# var = 1 
# while number > 1:
#     for i in range(1,number+1):
#         var = var * i
#     break
# print(f"Giai thừa của số {number} là: {var}")
#Cách 1
# number = int(input("Enter a positive number: "))
# var = 1
# while number>=1: 
#     for i in range(1,number+1):
#         var = var * i
#     break
# print(f"Factorial of {number} is: {var}")
# #Cách 2: 
number = int(input("Enter a negative number: "))
var = 1
while number<1:
    print("Invalid number. Please enter a positive number")
    number = int(input("Enter a negative number: "))
for i in range(1,number+1):
    var = var * i
print(f"Factorial of {number} is: {var}")