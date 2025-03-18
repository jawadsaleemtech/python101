
# Arithmetic Addition
print(10 + 5)

float1 = 13.65
float2 = 3.40
print(float1 + float2)

num = 20
flt = 10.5
print(num + flt)

# Arithmetic Floor Division
print( 43 // 10)

float1 = 5.5
float2 = 4.5
print(float1 // float2)
print(12.4 // 2)


# Modulo

print(10 % 2)

var = 28
print(var % 10)

print(-28 % -10)  # The remainder is negative if the right-hand operand is negative
print(-28 % 10)   # The remainder is positive if the right-hand operand is positive
print(28 % -10)   # The remainder is negative if the right-hand operand is negative

print(34.4 % 2.5)  # The remainder can be a float


# Exponent

print(2 ** 3)  

float1 = 13.65
float2 = 3.40
print(float1 ** float2)  

num = 20
flt = 2.0
print(num ** flt)  


# Precedence

# Different precedence
print(10 - 3 * 2)  # Multiplication computed first, followed by subtraction

# Same precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by division
print(3 / 20 * 5)  # Division computed first, followed by multiplication


# Parentheses

print((10 - 3) * 2) 
print((18 + 2) / (10 % 8))


# Compound Assignment Operators


num = 10
num += 5    # num=num+5
print(num)  

num -= 3    # num=num-3
print(num)  

num *= 2    # num=num*2
print(num)  

num /= 2    # num=num/2
print(num)  

num //= 3   # num=num//3
print(num)  

num %= 3    # num=num%3
print(num) 

num **= 2   # num=num**2
print(num) 