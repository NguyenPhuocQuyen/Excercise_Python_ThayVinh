number = int(input("Nhập một số bất kỳ: "))
var = 0
for i in range(1, number+1):
    if i % 2 == 0:
        print(i, end = " ")
        var = var + i
print (f"\nTổng các số chẵn là : {var}")
