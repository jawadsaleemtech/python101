random_set = {"Jawad", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  



empty_set = set()
print(empty_set)

random_set = set({"Jawad", 1408, 3.142, (True, False)})
print(random_set)



test_set = {"Jawad", 1408, 3.142, (True, False)}
test_lst = ["Jawad", 1408, 3.142, (True, False)]
test_dic = {1: "Jawad", 2: 1408, 3: 3.142, 4: (True, False)}
test_tup = ("Jawad", 1408, 3.142, (True, False))

print(type(test_set))  
print(type(test_lst))  
print(type(test_dic))  
print(type(test_tup))  


# Adding 
empty_set = set()
print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([2, 2, 3, 4, 5, 5, 5, 6])
print(empty_set)


# Deleting
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

random_set.discard(1408)
print(random_set)

random_set.discard((True, False))
print(random_set)


# Set Comprehension
squares_set = {x**2 for x in range(10)}
print(squares_set)