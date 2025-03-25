# Import and From

In this example, we demonstrate two ways of importing functions from one module into another in Python.

### 1. Using `import module_name`
When you use `import module_name`, you import the entire module and access its functions, classes, or variables using the module name as a prefix.

### 2. Using `from module_name import ...`
When you use `from module_name import ...`, you import specific elements (functions, classes, or variables) directly into the current namespace.

### Code Example

```python
# module_a.py

def say_hello():
    print("Hello from module_a!")

def say_goodbye():
    print("Goodbye from module_a!")



# module_b.py

import module_a          # Importing the entire module
from module_a import say_hello  # Importing only the specific function

# Using both ways
module_a.say_goodbye()  # Accessing the function using the module name
say_hello()  # Directly using the imported function
```