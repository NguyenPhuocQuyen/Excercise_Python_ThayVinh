string = str(input("Please enter a string: "))
location_index_start = int(input("Please enter a location start: "))
location_index_end = int(input("Please enter a location end: "))

substring = string[location_index_start:location_index_end]

print(f"Substring is: {substring}")

