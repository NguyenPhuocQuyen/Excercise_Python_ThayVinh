#Way_1
"""a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

max_number = max(a, b, c)
min_number = min(a, b, c)

print(f"Số lớn nhất là {max_number}")
print(f"Số nhỏ nhất là {min_number}")"""

#Way_2
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a > b and a > c:
    print(f"Số lớn nhất là {a}")
if b > c and b > a:
    print(f"Số lớn nhất là {b}")
if c > a and c > b:
    print(f"Số lớn nhất là {c}")
if a < b and a < c:
    print(f"Số nhỏ nhất là {a}")
if b < c and b < a:
    print(f"Số nhỏ nhất là {b}")
if c < a and c < b:
    print(f"Số nhỏ nhất là {c}")        
