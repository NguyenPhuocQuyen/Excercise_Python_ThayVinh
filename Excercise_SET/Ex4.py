def present_all(list_set):
    present = list_set[0].union(*list_set[1:])
    return present
set_1 = {2,3,4,"Python","C++"}
set_2 = {3,4,5,"Python","C#"}
set_3 = {4,5,6,"Python","JS"}

list_set = [set_1, set_2, set_3]
result = present_all(list_set)
print(f"Present in all sets is: {result}")