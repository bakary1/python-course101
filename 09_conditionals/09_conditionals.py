########################
## Day 8 - Conditionals
########################

## Exercises: Level 1

# 1. user input with conditionals
user_age = int(input("Please enter your age:"))
years_left = 18 - user_age

if user_age >= 18:
    print("You are old enough to learn to drive")

elif years_left == 1:
    print(f"You need to wait {years_left} more year before you start")
else:
    print(f"You have to wait {years_left} more years before you start")

# 2. Compare ages
your_age = int(input("Enter your age:"))
my_age = 34
age_diff = abs(your_age - my_age)

if your_age > my_age:
    if age_diff == 1:
        print(f"You are {age_diff} year older than me")
    else:
        print(f"You are {age_diff} years older than me")
elif my_age > your_age:
    if age_diff == 1:
        print(f"I am {age_diff} year older than you")
    else:
        print(f"I am {age_diff} years older than you")

# 3. Two numbers using input
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")

## Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
score = int(input("Enter the student's score:"))

if score >= 90 and score <= 100:
    print("Student grade: A")
elif score >= 80 and score <= 89:
    print("Student grade: B")
elif score >= 70 and score <= 79:
    print("Student grade: C")
elif score >= 60 and score <= 69:
    print("Student grade: D")
else:
    print("Student grade: F")

# 2. Check the season
current_month = input("Enter the current month:").title()

if current_month in ["September", "October", "November"]:
    print("Current season: Autumn")
elif current_month in ["December", "January", "February"]:
    print("Current season: Winter")
elif current_month in ["March", "April", "May"]:
    print("Current season: Spring")
elif current_month in ["June", "July", "August"]:
    print("Current season: Summer")
else:
    print("Please enter a valid month")

# 3. Check the fruits
fruits = ["banana", "orange", "mango", "lemon"]

user_fruit = input("Enter your fruit of choice:")
if user_fruit.lower() not in fruits:
    fruits.append(user_fruit.lower())
else:
    print("That fruit already exists in the list")

    ## Exercises: Level 3

    person = {
        "first_name": "Asabeneh",
        "last_name": "Yetayeh",
        "age": 250,
        "country": "Finland",
        "is_married": True,
        "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
        "address": {"street": "Space street", "zipcode": "02210"},
    }

# 1. Check if the person dictionary has skills key
if person.get("skills"):
    length = len(person["skills"])
    print(person["skills"][(length // 2)])
else:
    print("The person don't have any recorded skills")

# 2. Check if the person dictionary has skills key
if "skills" in person:
    if "Python" in person["skills"]:
        print("The person has Python skills")
    else:
        print("The person does not have Python skills")
else:
    print("The person does not have a skills key")

# 2. If a person skills has only JavaScript and React
if "skills" in person:
    if {"React", "JavaScript"} == set(person["skills"]):
        print("He is a frontend developer")
    elif {"Node", "Python", "MongoDB"}.issubset(set(person["skills"])):
        print("He is a backend developer")
    elif {"React", "Node", "MongoDB"}.issubset(set(person["skills"])):
        print("He is a fullstack developer")
    else:
        print("Unkown title")
else:
    print("The person does not have any recorded skills")

# 3. If the person is married and if he lives in Finland, print the information
if person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married."
    )
