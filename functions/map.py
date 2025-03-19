num_list = [0, 1, 2, 3, 4, 5]

# Using a lambda function directly with map
squared_numbers = map(lambda num: num * num, num_list)

# Convert the map object to a list
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  