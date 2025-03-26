# EAFP "Easier to Ask for Forgiveness than Permission" Example
def get_value_from_dict(my_dict, key):
    try:
        return my_dict[key]  # Try to get the value for the key
    except KeyError:
        return None  # If the key doesn't exist, handle the error

# Using the function
my_dict = {"name": "Alice", "age": 30}
print(get_value_from_dict(my_dict, "name"))  # Outputs: Alice
print(get_value_from_dict(my_dict, "address"))  # Outputs: None



# LBYL (Look Before You Leap)  Example
def get_value_from_dict(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

# Using the function
print(get_value_from_dict(my_dict, "name"))  # Outputs: Alice
print(get_value_from_dict(my_dict, "address"))  # Outputs: None
