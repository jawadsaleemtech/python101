my_string = "This is MY string!"
print(my_string[0:4]) 
print(my_string[1:7])
print(my_string[8:len(my_string)])



my_string = "123 45 67 89abcd!"
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above



my_string = "This is MY string!"
print(my_string[:8])   # All the characters before 'M'
print(my_string[8:])   # All the characters starting from 'M'
print(my_string[:])    # The whole string
print(my_string[::-1]) # The whole string in reverse (step is -1)