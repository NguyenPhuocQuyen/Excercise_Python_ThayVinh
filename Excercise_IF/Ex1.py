# Way_1
"""a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
if a > b and a > c: 
    print(f"Số {a} là số lớn nhất")
if b > a and b > c: 
    print(f"Số {b} là số lớn nhất")
if c > a and c > b: 
    print(f"Số {c} là số lớn nhất")"""
#Way_2
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

max_number = max(a, b, c)

print(f"Số lớn nhất là {max_number}")