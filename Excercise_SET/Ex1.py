def value_set(set1,set2):
    common = set1.intersection(set2)
    return common
set1 = {1,2,3,4,5,6,7,"dut","BKDN"}
set2 = {3,5,7,"BKDN","Telephone"}
result = value_set(set1, set2)
print(f"Element common is: {result}")