"""
    Purpose: Built-In string functions
	
	capitalize: Converts the first character to uppercase and the rest to lowercase.
	casefold: Converts the string to lowercase for case-insensitive comparisons.
	encode: Converts the string into a bytes object using a specified encoding.
	index(substring): Returns the index of the first occurrence of a substring (raises an error if not found).
	isalnum: Returns True if the string contains only alphanumeric characters (letters and numbers).
	isalpha: Returns True if the string contains only letters (no numbers or special characters).
	isdecimal: Returns True if the string contains only decimal characters (0-9).
	isdigit: Returns True if the string contains only digits (including superscripts and subscripts).
	isidentifier: Returns True if the string is a valid Python identifier (variable/function name).
	islower: Returns True if all characters in the string are lowercase.
	isnumeric: Returns True if the string contains only numeric characters (including fractions, subscripts, etc.).
	isprintable: Returns True if all characters in the string are printable.
	isspace: Returns True if the string contains only whitespace characters (spaces, tabs, newlines).
	istitle: Returns True if the string follows title case (each word starts with an uppercase letter).
	isupper: Returns True if all characters in the string are uppercase.
	join(iterable): Concatenates elements of an iterable (list, tuple) into a string with the given separator.
	lower: Converts all characters in the string to lowercase.
	lstrip: Removes leading whitespace (or specified characters) from the string.
	maketrans: Creates a translation table for use with translate().
	partition(separator): Splits the string into three parts: before, separator, and after.
	replace(old, new): Replaces all occurrences of old with new in the string.
	rfind(substring): Returns the highest index of a substring (returns -1 if not found).
	rindex(substring): Returns the highest index of a substring (raises an error if not found).
	rjust(width): Right-aligns the string within a given width, padding with spaces or a specified character.
	rpartition(separator): Splits the string into three parts: before, separator, and after (starting from the right).
	rsplit(separator):Splits the string at the specified separator and returns a list
	rstrip(): Returns a right trim version of the string
	split(separator): Splits the string at the specified separator and returns a list
	splitlines(): Splits the string at line breaks and returns a list
	strip(): Returns a trimmed version of the string
	swapcase(): In swap cases, the lowercase becomes the uppercase, and vice versa
	title(): Converts the first character of each word to uppercase
	upper(): Converts a string to uppercase
	center(width): Returns a centered string 
	count(substring): Returns the number of times a specified value occurs in a string
	endswith(suffix): Returns True if the string ends with the specified value
	find(substring): Searches the string for a specified value and returns the position of where it was found
"""

# Search

random_str = "this is jawad"
print(random_str.find("wad"))
print(random_str.find("is",9,12))


# Replace

new_str = random_str.replace("jawad","python")
print(new_str)


# Upper Lower
print("UpperCase".upper())
print("LowerCase".lower())


# join strings
str_list = ['a', 'b', 'c']
print('>>'.join(str_list)) # joining strings with >>
print('<<'.join(str_list)) # joining strings with <<
print(', '.join(str_list)) # joining strings with comma and space
print(str_list) # joining strings with comma and space


str_list = ['a', 'b', 'c']
string = "abc"
str_tuple = ('a', 'b', 'c') 
print(', '.join(str_list))  # joining strings with comma and space
print(', '.join(string))    # joining strings with comma and space
print(', '.join(str_tuple)) # joining strings with comma and space


# Fromatting
print("\nFormatting")

str1 = "Learn Python {version} from {cname}".format(version=3,cname="Jawad")
print(str1)

str2 = "Learn Python {0} from {1}".format(3,"Jawad")
print(str2)

str3="Learn Python {} from {}".format(3,"Jawad")
print(str3)

# Built-In Functions
print("\nBuilt-In Functions")

# capitalize()
print("hello world".capitalize())

# casefold()
print("HELLO World".casefold())

# center()
print("hello".center(20, '-'))

# count()
print("hello world".count('l'))

# encode()
print("hello".encode())

# endswith()
print("hello".endswith("lo"))

# expandtabs()
print("hello\tworld".expandtabs(4))

# find()
print("hello world".find('world'))

# format()
print("Hello, {name}!".format(name="John"))

# index()
print("hello world".index('world'))

# isalnum()
print("hello123".isalnum())

# isalpha()
print("hello".isalpha())

# isdecimal()
print("123".isdecimal())

# isdigit()
print("123".isdigit())

# isidentifier()
print("variable1".isidentifier())

# islower()
print("hello".islower())

# isnumeric()
print("123".isnumeric())

# isspace()
print("   ".isspace())

# istitle()
print("Hello World".istitle())

# isupper()
print("HELLO".isupper())

# join()
print(", ".join(["apple", "banana", "cherry"]))

# ljust()
print("hello".ljust(10, '-'))

# lower()
print("HELLO World".lower())

# lstrip()
print("   hello".lstrip())

# partition()
print("hello world".partition(" "))

# replace()
print("hello world".replace("world", "Python"))

# rfind()
print("hello world world".rfind('world'))

# rindex()
print("hello world world".rindex('world'))

# rjust()
print("hello".rjust(10, '-'))

# rpartition()
print("hello world world".rpartition('world'))

# rsplit()
print("hello world world".rsplit(' ', 1))

# rstrip()
print("hello   ".rstrip())

# split()
print("hello world".split())

# splitlines()
print("hello\nworld".splitlines())

# startswith()
print("hello".startswith("he"))

# strip()
print("   hello   ".strip())

# swapcase()
print("HeLLo WoRLd".swapcase())

# title()
print("hello world".title())

# upper()
print("hello".upper())
