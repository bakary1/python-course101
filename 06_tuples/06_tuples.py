########################
## Day 6 - Tuples
########################

## Exercises: Level 1

# 1. Create an empty tuple
tpl = ()

# 2. Create a tuple containing names of your siblings
sisters = ("Anna", "Jennifer")
brothers = ("Bo", "Victor")
siblings = sisters + brothers

# 3. How many siblings do you have?
print(f" I have {len(siblings)} siblings")

# 4. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family = siblings + ("Mamma", "Pappa")

## Exercises: Level 2

# 1. Unpack siblings and parents from family_members
siblings = family[:-2]
parents = family[-2:]

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples
fruits = ("banana", "apple", "kiwi")
vegetables = ("cucumber", "salad", "tomato")
animal_products = ("beef", "turkey")

food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt[len(food_stuff_lt) // 2]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
food_stuff_lt[:3]
food_stuff_lt[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

if "Estonia" in nordic_countries:
    print("Estonia is a nordic country")
else:
    print("Estonia is not a nordic country")
