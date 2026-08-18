####################################
## Day 14 - Higher Order Functions
####################################

## Exercises: Level 2

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map to create a new list by changing each country to uppercase in the countries list
new_countries = list(map(lambda x: x.upper(), countries))

# 2. Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda x: x**2, numbers))

# 3. Use map to change each name to uppercase in the names list
upper_names = list(map(lambda name: name.upper(), names))

# 4. Use filter to filter out countries containing 'land'.
list(filter(lambda x: "land" in x, countries))

# 5. Use filter to filter out countries having exactly six characters.
list(filter(lambda country: len(country) == 6, countries))
