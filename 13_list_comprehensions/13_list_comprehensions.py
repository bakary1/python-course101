################################
## Day 13 - List Comprehensions
################################

## Exercises: Level 1

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered = [number for number in numbers if number <= 0]

# 2. Flatten the following list of lists of lists to a one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [number for row in list_of_lists for number in row]

# 5. Flatten the following list to a new list:
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

output = [
    [country.upper(), country.upper()[:3], capital.upper()]
    for [(country, capital)] in countries
]

# 6. Change the following list of lists to a list of concatenated strings:
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]

[f"{first_name} {last_name}" for [(first_name, last_name)] in names]
