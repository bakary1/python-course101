########################
## Day 8 - Dictionaries
########################

## Exercises: Level 1

# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog.update({"name": "Billy", "color": "black", "age": 5})

# 3. Create a student dictionary
student = {
    "first_name": "Hannah",
    "last_name": "Ceder",
    "gender": "female",
    "age": 35,
    "marital_status": "single",
    "skills": ["python", "sql", "databricks"],
    "country": "Sweden",
    "city": "Stockholm",
    "address": "Vasastan",
}

# 4. Get the length of the student dictionary
print(f"The length of the student dictionary: {len(student)}")

# 5. Get the value of skills and check the data type, it should be a list
type(student["skills"])

# 6. Modify the skills values by adding one or two skills
new_skills = ["dbt", "airflow"]
for skill in new_skills:
    student["skills"].append(skill)

# 4. Get the dictionary keys as a list
student.keys()

# 5. Get the dictionary values as a list
student.values()

# 6. Change the dictionary to a list of tuples using items() method
student.items()

# 7. Delete one of the items in the dictionary
student.pop("address")

# 8. Delete one of the dictionaries
del dog
