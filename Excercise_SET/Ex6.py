def subsets(set1, number):
    result = set()   
    for element in set1:
        if len(element) <= number:
            result.add(element)
    return result
set1 = {"Python", "aaaaaaa", "aaa", "vvvv","bb","cc"}
number = 3
result = subsets(set1, number)
print(result)

