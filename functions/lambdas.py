"lambda parameters: expression"

triple = lambda num : num * 3
print(triple(10))


print_triple = lambda num: print(num * 3)
print_triple(2)


hardcoded_triple = lambda: 10 * 3
print(hardcoded_triple())


concat_strings = lambda a, b, c: a[0] + b[0] +c[0]
print(concat_strings("World", "Wide", "Web"))

# Conditional Statements with Lambda
my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))

is_even = lambda num: "Even" if num % 2 == 0 else "Odd"
print(is_even(3))