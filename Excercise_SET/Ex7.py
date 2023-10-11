def check_list(set1, set2):
   return set1.issubset(set2) or set2.issubset(set1)
set1 = {2,3,4,"Python","C++"}
set2 = {2,"Python","C++"}
result = check_list(set1, set2)
print(f"Result is: {result}")
    