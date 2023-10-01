# Cách 1
# number = int(input("Nhập một số cho trước: "))
# number_var = 0

# while number > 0: 
#     var = number % 10
#     number_var = number_var + var 
#     number = number // 10 
# print(number_var)

# Cách 2
# Vòng lặp for chỉ lặp qua kiểu chuỗi hoặc kiểu list không lặp qua số nguyên
# nên ta phải chuyển đổi qua kiểu chuỗi 
number = int(input("Nhập một số: "))
var = 0
for i in str(number):
     var = var + int(i)
print(f"Tổng các chữ số riêng lẻ là: {var}")
 

