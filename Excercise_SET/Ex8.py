def check_number(set1):
    for number in set1:
        if number % 2 != 0:
            return False
    return True
# set1 = {1,2,3,4,5,6,7,8,9,10,11}
set1 = {2,4,6,8,10}
result = check_number(set1)
if result: 
    print("True")
else:
    print("False")    