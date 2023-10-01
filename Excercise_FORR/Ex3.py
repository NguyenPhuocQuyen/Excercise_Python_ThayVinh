# # Cách 1: Dùng hàm 
# element = [7,3,9,5]

# max_number = max(element)
# print(f"Số lớn nhất trong chuỗi đã cho là: {max_number}")

#Cách 2: Dùng gán 
# element = list(map(int, input("Nhập vào một danh sách số:").strip().split(" ")))
element = [7,5,4,2,5,7,14] 
max_number = element[0]

for i in range(len(element)):
    if element[i] > max_number:
        max_number = element[i]
print(f"\nPhần tử lớn nhất trong mảng là {max_number}")
