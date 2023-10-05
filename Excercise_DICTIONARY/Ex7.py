# age = {
#     'A':23,
#     'C':14,
#     'D':12,
#     'E':15,
#     'F':26,
#     'G':24
# }
# age_value = age.values()
# dict_age_value = list(age_value)
# max_temp = max(dict_age_value)
# print(f'Maximum value in a dictionary is: {max_temp}.')

#Cách 2
# age = {
#     'A':23,
#     'C':14,
#     'D':12,
#     'E':15,
#     'F':26,
#     'G':24
# }

# age_value = list(age.values())
# max_temp = None
# for check in age_value:
#     if max_temp is not None and check > max_temp:
#         max_temp = check
# print(f'Maximum value in a dictionary is: {max_temp}.')
