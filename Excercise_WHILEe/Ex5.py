var_number = 0
count_number = 0
while True:
    number = float(input("Enter the number: "))
    if number == -1:
        break
    else:
        count_number += 1
        var_number = var_number + number
print(f"Their average a serial number is: {var_number/count_number}")    