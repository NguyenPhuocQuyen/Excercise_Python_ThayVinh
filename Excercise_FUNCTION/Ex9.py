import math
def calculate_median(*args):
        median = sum(args)/(len(args))
        return median
result = calculate_median(1,2,3,4,5,6)
print(result)