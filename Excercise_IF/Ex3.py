Year = int(input("Nhập vào số năm cần xác định: "))
if (Year % 400 == 0) or ((Year % 4 == 0) and (Year % 100 != 0)):
    print (f"Năm {Year} là năm nhuận")
else:
    print(f"Năm {Year} không phải là năm nhuận")