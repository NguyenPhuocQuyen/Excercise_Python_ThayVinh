import math
# while True:
#     number = int(input("Nhập một số cần kiểm tra: "))
#     if number == 2:
#         print("Số 2 là số nguyên tố")
#     while number>1: 
#         for i in range(2, number):
#             if number % i == 0:
#                 print(f"Số {number} không phải là số nguyên tố")
#             else:
#                 print(f"Số {number} là số nguyên tố")
#             break
#         break
#     else:
#         print("Không hợp lệ")
#         continue

#Cách 1
number = int(input("Enter a number to check: "))

while number<=1:
    print("No prime number")
    number = int(input("Enter a prime number: "))
for i in range(2, int(number**0.5)+1):
    if number % i == 0:
        print(f"Number {number} is not a prime number")
        break
else: 
    print(f"Number {number} is a prime number")
