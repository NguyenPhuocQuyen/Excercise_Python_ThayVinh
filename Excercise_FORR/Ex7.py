# number = int(input("Nhập số cần tìm số đảo ngược: "))
# temp_number = number 
# reverse_number = 0 

# while number > 0:
#     last_number = number % 10
#     reverse_number = reverse_number * 10 + last_number
#     number = number // 10 

# print(f"Số đảo ngược của {temp_number} là: {reverse_number}")

#Cách 2

number = input("Nhập số cần tìm số đảo ngược: ")
reverse_number = number[::-1]
print(reverse_number)
# print(f"Số đảo ngược của {number} là số: {reverse_number}")

