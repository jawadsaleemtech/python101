# union

# Define two sets
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

# Find and print union of two set
print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

# intersection

# Define two sets
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

# Find and print intersection of two set
print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))


# Difference
# Define two sets
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

# Find and print difference of two set
print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))


print("\nSymmetric Difference")
# Symmetric Difference
# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Using symmetric_difference() method
sym_diff_method = set_A.symmetric_difference(set_B)
print("Symmetric difference using symmetric_difference() method:", sym_diff_method)

# Using ^ operator
sym_diff_operator = set_A ^ set_B
print("Symmetric difference using ^ operator:", sym_diff_operator)

# Additional options
sym_diff_reverse_method = set_B.symmetric_difference(set_A)
sym_diff_reverse_operator = set_B ^ set_A

print("Symmetric difference using set_B.symmetric_difference(set_A):", sym_diff_reverse_method)
print("Symmetric difference using set_B ^ set_A:", sym_diff_reverse_operator)