# while True: 
#     for i in range(5, 10):
#         print(f"\nMultiplication table {i} is: ")
#         for j in range( 1, 11):
#             mul = i*j
#             print(f"{i} * {j} = {mul}")
#     break

i = 5
while i <= 9: 
    print(f"\nMultiplication table {i} is: ")
    j = 1
    while j <= 10:
        mul = i * j
        print(f"{i} * {j} = {mul}")
        j = j + 1
    i = i+ 1

