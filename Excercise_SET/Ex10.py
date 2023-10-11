def disjoint_check(set1,set2):
    return set1.isdisjoint(set2) or set2.isdisjoint(set1)
set1 = {2,3,4,"Python","C++"}
set2 = {3,4,5,"Python","C#"}
# set2 = {"aaa","bbb",5,6}
result = disjoint_check(set1,set2)
if result:
    print("True")
else:
    print("False")