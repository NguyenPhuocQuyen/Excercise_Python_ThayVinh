def revered_set(input_set):
    reserved = list(input_set)[::-1]
    return reserved
# input_set = {"python","java","js","C++","python","java","C#"}
input_set = {1,2,2,3,4,5,6,6,7,8,7,8,9}

print(revered_set(input_set))

