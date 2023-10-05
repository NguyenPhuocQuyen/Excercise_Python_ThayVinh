import random 
while True: 
    number = random.randint(1,100)
    if number % 7 == 0:
        print(f"Number {number} divisible by 7. Stop ! ")
        break 
    else: 
        print(f"Number {number} not divisible by 7")
