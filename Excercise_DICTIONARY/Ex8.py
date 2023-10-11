price = {
    'Cake': 5000,
    'Pen': 2000,
    'Pencil': 1000,
    'Book':10000,
    'Bycicle': 50000,
}
value = list(price.values())
value.sort(reverse=True)
# value = sorted(value, reverse=False)
print(value)

# #Cách 2
# price = {
#     'Cake': 5000,
#     'Pen': 2000,
#     'Pencil': 1000,
#     'Book':10000,
#     'Bycicle': 50000,
# }
# value = list(price.values())
# max_value = None
# for check in value:
#     if max_value is not None and check > max_value:
#         check = max_value
# print(max_value)

