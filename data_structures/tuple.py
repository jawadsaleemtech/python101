# similar to list but cant be changes ()
car = ("Ford", "Raptor", 2019, "Red")
# car.append("Honda")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])


# Merging Tuples

hero_names = ("Batman", "Wonder Woman", "Superman")
hero_ages = (35, 80, 40)
hero_powers = ("Martial Arts", "Super Strength", "Flight")
merged_heroes_info = hero_names + hero_ages + hero_powers
print(merged_heroes_info)


# Nested Tuples
hero1 = ("Batman", "Bruce Wayne", 35, 85.5)
hero2 = ("Wonder Woman", "Diana Prince", 80, 99.9)
awesome_team = (hero1, hero2)
print(awesome_team)

# Search 
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Tokyo" in cities)
print("Moscow" in cities)


# index
cities_set1 = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities_set1.index("Tokyo"))

cities_set2 = (
    ("London", 8.9, "UK"),
    ("Paris", 2.1, "France"),
    ("Los Angeles", 3.9, "USA"),
    ("Tokyo", 14.0, "Japan")
)

tokyo_index = [city[0] for city in cities_set2].index("Tokyo")
print(f"Index of Tokyo: {tokyo_index}")