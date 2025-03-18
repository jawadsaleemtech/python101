original_list = [1, 2, 3]
same_reference_list = original_list
different_list = [1, 2, 3]
reordered_list = [1, 3, 2]

print(original_list is same_reference_list) 
print(original_list is different_list) 
print(original_list == different_list)  
print(original_list == reordered_list)  

# Example with integers
first_number = 10
second_number = 20
third_number = 10
print(first_number is not second_number)  
print(first_number is not 10) 

same_reference_number = first_number 
print(same_reference_number is first_number) 