# Creating an empty dictionary
empty_dict = {} 
print(empty_dict)


phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)


# Alternative approach
phone_book = {'Batman': 468426,
			  'Cersei': 237734,
             'Ghostbusters': 44678}
print(phone_book)



# Accessing Values
print(phone_book.get("Batman"))

print(phone_book.keys())  # Output: dict_keys(['Batman', 'Cersei', 'Ghostbusters'])

# using lists
keys_list = list(phone_book.keys())
print(keys_list)  # Output: ['Batman', 'Cersei', 'Ghostbusters']

# using for loop
for key in phone_book:
    print(key)
    
# using unpacking
print(*phone_book)  # Output: Batman Cersei Ghostbusters



# Adding Elements
phone_book['SuperMan'] = 12345
phone_book['SuperMan'] = 112233
print(phone_book)  


# Deleting Elements
print(phone_book)
del phone_book["Batman"]
print(phone_book)


cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

lastAdded = phone_book.popitem()
print(lastAdded)

print(phone_book)


# Length
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(len(phone_book))


# update
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}
print(phone_book)
# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)



# Dictionary Comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n*2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)