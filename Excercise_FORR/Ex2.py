number = int(input("Nhập một số từ bàn phím: "))
var = 0
for i in range(1, number+1):
    if (i % 3 == 0) or (i % 5 == 0):
        print(i, end = " ")
        var = var + i
print(f"\nTổng các số chia hết cho 3 hoặc 5 là: {var}")
    