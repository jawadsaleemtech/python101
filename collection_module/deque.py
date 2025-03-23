# from collections import deque
# import string
# print(string.ascii_lowercase)
# d = deque(string.ascii_lowercase)
# print(d)
# for letter in d:
#     print(letter)
    

from collections import deque
import string

d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
d.append("bork")
print(d)


d.appendleft("test")
print(d)


d.rotate(1) # rotate 1 time to right
print(d)
