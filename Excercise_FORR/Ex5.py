number = int(input("Nhập một số: "))
var = 1
for i in range(1, number+1):
    var = var * i
print(f"Giai thừa của {number} là: {var}")