def calculate_area(length,width):
    if length <=0 or width <= 0: 
        return "No valid"
    elif length == width:
        return (f'This is a square shape and have area is: {length*width}')
    else: 
        area = length * width
        return (f"Area_rectangle is: {area}")
length = float(input("Please enter length: "))    
width = float(input("Please enter width: "))    
area_rectangle = calculate_area(length,width)
print(area_rectangle)

