squares = {1: 1, 2: 4, 3: 9, 4: 16}
new_squares = {i+i:j+1 for (i,j) in squares.items()} #Your code here
print(new_squares) 

# {2: 2, 4: 5, 6: 10, 8: 17}