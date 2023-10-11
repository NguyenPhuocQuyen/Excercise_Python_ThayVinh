def exclusive(set1, set2):
    exclusive_element = set1.symmetric_difference(set2)
    return exclusive_element
set1 = {2,3,4,"Python","C++"}
set2 = {3,4,5,"Python","C#"}
result = exclusive(set1, set2)
print(f"Exclusive to each set is: {result}")