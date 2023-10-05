string = str(input("Please enter a string: "))
location_index = int(input("Please enter a location: "))
if 0 <= location_index < len(string):
    character = string[location_index]
    print(f"Character is: {character}")
else:
    print("No valid character")