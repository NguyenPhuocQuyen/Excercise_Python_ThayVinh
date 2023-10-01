import math
number = int(input("Nhập một số cần kiểm tra: "))

if number == 2:
    print(f"Số {number} là số nguyên tố")

else:
    for i in range(2,  int(math.sqrt(number))+1):
        print(i)
        if number % i == 0:
            print(f"Số {number} không phải là số nguyên tố")
            break 
    else:
        print(f"Số {number} phải là số nguyên tố")
