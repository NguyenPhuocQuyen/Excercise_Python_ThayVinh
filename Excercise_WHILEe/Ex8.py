list = []
var = 0 
while True: 
    number = int(input("Enter the number: "))
    if number == 0: 
        break
    else: 
        list.append(number)
for i in list:
    if i % 3 == 0:
        var = var + i
print(f"Sum of numbers divisible by 3 is: {var}")
