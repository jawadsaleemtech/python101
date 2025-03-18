print("| A     | B     | AND    | OR     | NOT A  | NOT B  |")
print("| ----- | ----- | ------ | ------ | ------ | ------ |")
print("| True  | True  |", True and True, "  |", True or True, "  |", not True, " |", not True, " |")
print("| True  | False |", True and False, " |", True or False, "  |", not True, " |", not False, "  |")
print("| False | True  |", False and True, " |", False or True, "  |", not False, "  |", not True, " |")
print("| False | False |", False and False, " |", False or False," |", not False, "  |", not False, "  |")



# Bit Value

print(10 + True)
print(10 + False)
print (True + False)

# Compound Logical Assignment Operator

x = True
y = False
x &= y     # x = x and y
print(x)  

z = True
z |= y # z = z or y
print(z)