name = "Ned"

def func():
    name = "Stark"

func()
print(name)  # The value of 'name' remains unchanged.


# Global

planet = "Earth"

def print_planet():
    print("We live on", planet)

print_planet()  

def change_planet():
    global planet  
    planet = "Mars"

change_planet()
print_planet() 