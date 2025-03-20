# Average of numbers in list

my_list = [10,20,30,40,50]
sum = 0
for i in my_list:
    sum += int(i)
    
average = sum/len(my_list)

print(f"The average of {my_list} is {average}")

# Looping a list

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
# Iterator traverses to the last index of the list
for i in range(0, len(float_list)):  
    print (float_list[i])
    
# Iterator Approach
string_list = ["Hello", "World", "Jawad", "Learning", "Blog"]

for str1 in string_list:  # Iterator traverses to the last index of the list
    print(str1)


# Parsing individual Chars

test_string = "Hello"
for i in range(0, len(test_string)): #access characters using indexing
  print(test_string[i]) 

test_string = "World"
for i in test_string: #access characters using the iterator directly
  print(i)


for i in range(1, 11, 3):
  print(i)

for i in range(10, 0, -1):  
    print(i)
    
for i in range(1,11):
	print(i)

for i in range(3): 
    print("First: Hello, world!")

for i in range(0, 3):
    print("Second: Hello, world!")

for i in range(0, 3, 1):
    print("Third: Hello, world!")

for i in range(3, 0, -1):  
    print("Fourth: Hello, world!")
    

# Even or Odd

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")