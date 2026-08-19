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

# 6. Use filter to filter out countries containing six letters and more in the country list.
list(filter(lambda x: len(x) >= 6, countries))

# 7. Use filter to filter out countries starting with an 'E'
list(filter(lambda x: x.startswith("E"), countries))

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
from typing import Any


def get_string_lists(values: list[Any]) -> list[str]:
    return list(filter(lambda item: isinstance(item, str), values))


get_string_lists(["hello", 5])

# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce

reduce(lambda x, y: x + y, numbers)

# 11. Use reduce to concatenate all the countries and to produce this sentence
sentence = ", are north European countries."
(
    reduce(lambda x, y: x + " " + y, countries[:-1])
    + " "
    + "and"
    + " "
    + countries[-1]
    + sentence
)
