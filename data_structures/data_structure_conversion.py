# Converting-to-a-list
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# keys only
star_wars_list = list(star_wars_dict)  # Converting from dictionary
print(star_wars_list)


# keeping keys and values
star_wars_list = list(star_wars_dict.items())
print(star_wars_list)



# Converting to a tuple

# List of Star Wars characters and a number
star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)

# Tuple of Star Wars characters and a number
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)

# Dictionary mapping numbers to Star Wars characters
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# Converting the list to a tuple
star_wars_tuple_from_list = tuple(star_wars_list)
print(star_wars_tuple_from_list)

# Converting the tuple to a new tuple (redundant but for demonstration)
star_wars_tuple_from_tup = tuple(star_wars_tup)
print(star_wars_tuple_from_tup)

# Converting the keys of the dictionary to a tuple
star_wars_tuple_from_keys = tuple(star_wars_dict.keys())
print(star_wars_tuple_from_keys)

# Converting the values of the dictionary to a tuple
star_wars_tuple_from_values = tuple(star_wars_dict.values())
print(star_wars_tuple_from_values)

# Converting the items (key-value pairs) of the dictionary to a tuple
star_wars_tuple_from_items = tuple(star_wars_dict.items())
print(star_wars_tuple_from_items)


# Converting to a set

# List of Star Wars characters and a number
star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)

# Tuple of Star Wars characters and a number
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)

# Dictionary mapping numbers to Star Wars characters
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

# Converting the list to a set 
star_wars_set_from_list = set(star_wars_list)  
print(star_wars_set_from_list)

# Converting the tuple to a set 
star_wars_set_from_tup = set(star_wars_tup)  
print(star_wars_set_from_tup)

# Converting the keys of the dictionary to a set 
star_wars_set_from_dict = set(star_wars_dict)  
print(star_wars_set_from_dict)

# Converting the keys of the dictionary to a set
star_wars_set_from_dict = set(star_wars_dict.keys())
print(star_wars_set_from_dict)

# Converting the values of the dictionary to a set
star_wars_set_from_dict = set(star_wars_dict.values())
print(star_wars_set_from_dict)

# Converting the items of the dictionary to a set
star_wars_set_from_dict = set(star_wars_dict.items())
print(star_wars_set_from_dict)



# Converting to a dictionary
star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)


star_wars_dict = dict(star_wars_list) # Converting from list
print(star_wars_dict)

