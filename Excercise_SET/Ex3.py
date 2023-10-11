def present(set1,set2):
    present = set1.difference(set2)
    return present
set1 = {"Python","C++","C#","Js"}
set2 = {"Python","HTML","CSS","Js"}
result = present(set1,set2)
print(f"Present in the first set is: {result}")