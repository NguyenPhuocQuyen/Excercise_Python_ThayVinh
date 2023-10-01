def count_vowels(string):
    characters =[]
    count = 0
    vowels = ['u', 'e', 'o', 'a', 'i']
    for char in string:
        characters.append(char)
    for char in characters:
        if char in vowels:
            count += 1
    return count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
string = input("Please enter string: ")
print(count_vowels(string))
