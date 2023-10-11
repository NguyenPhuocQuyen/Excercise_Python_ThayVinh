#Cách 1:
max_number =[]
while True:
    number = float(input("Enter a serial number: "))
    if number == 0: 
        break
    else: 
      max_number.append(number)
max = max_number[0]
for i in range(len(max_number)):
    if max_number[i] > max:
        max = max_number[i]
print(f"Large number is: {max}")
# Cách 2

# max_number = float(input("Enter a max serial number: "))
# number = max_number 
# while number != 0:
#     number = float(input("Enter a serial number: "))
#     if number > max_number:
#         max_number = number
# print(f"Number is: {max_number}")
    