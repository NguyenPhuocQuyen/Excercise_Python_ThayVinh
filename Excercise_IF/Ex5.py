import math
#Cách 1: 
# number = int(input("Nhập số cần kiểm tra: "))
# temp_number = number 
# reserve_number = 0
# for i in range(2, number):
#     if number % i == 0:
#         print(f"Số {number} không phải là số xuôi ngược nguyên tố")
#         break
# else:
#     while number >= 1:
#         last_number = number % 10
#         reserve_number = reserve_number*10 + last_number
#         number = number // 10
#     if reserve_number == temp_number:
#         print(f"Số {temp_number} là số xuôi ngược nguyên tố")
#     else:
#         print(f"Số {temp_number} không phải là số xuôi ngược nguyên tố")
 #Cách 2: 
number = int(input("Nhập một số cần kiểm tra: "))
reserve_number = 0

for i in range(2,int(math.sqrt(number))):
    if number % i == 0:
        print(f"Số {number} không phải là số xuôi ngược nguyên tố")
        break
else:
    reserve_number = str(number)[::-1]
    if int(reserve_number) == number:
        print(f"Số {number} là số xuôi ngược nguyên tố")
    else:
        print(f"Số {number} không phải là số xuôi ngược nguyên tố")
"""Ví dụ với số 12321:

Lần lặp thứ nhất:

digit = 12321 % 10 = 1
reverse_number = 0 * 10 + 1 = 1
number = 12321 // 10 = 1232
Lần lặp thứ hai:

digit = 1232 % 10 = 2
reverse_number = 1 * 10 + 2 = 12
number = 1232 // 10 = 123
Lần lặp thứ ba:

digit = 123 % 10 = 3
reverse_number = 12 * 10 + 3 = 123
number = 123 // 10 = 12
Lần lặp thứ tư:

digit = 12 % 10 = 2
reverse_number = 123 * 10 + 2 = 1232
number = 12 // 10 = 1
Lần lặp thứ năm:

digit = 1 % 10 = 1
reverse_number = 1232 * 10 + 1 = 12321
number = 1 // 10 = 0"""

        