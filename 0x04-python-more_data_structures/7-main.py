#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

# Break the long line into multiple lines to comply with the 79 characters limit
new_dict = update_dictionary(
    a_dictionary, 'city', "San Francisco"
)
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
