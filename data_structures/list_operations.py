# Adding Elements
my_list=[]
my_list.append(1)
my_list.append(2)
my_list.append(2)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print(my_list)


my_list.insert(2,9)
print(my_list)


# pop
last_number = my_list.pop()
print(last_number)
print(my_list)

# delete
my_list.remove(2)
print(my_list)


# List Slicing
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5]) # 3,4,5
print(num_list[0::2]) # 1,3,5,7


# Retrieve Index
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the index 2


cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities) # True
print("London" not in cities) # False


# Sort
num_list = [20, 40, 10, 50.4, 30, 100, 5]
print(num_list)
li = sorted(num_list)
print(li)
print(num_list)