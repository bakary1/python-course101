########################
## Day 4 - Strings
########################

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
strings = "Thirty", "Days", "of", "Python"
new_string = (" ").join(strings)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strings = "Coding", "For", "All"
new_string = (" ").join(strings)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(f" The length of company: {len(company)}")

# 6. Change all the characters to uppercase letters using upper() method
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(f"Capitalize: {company.capitalize()}")
print(f"title: {company.title()}")
print(f"Swapcase: {company.swapcase()}")

# 9. Cut(slice) out the first word of Coding For All string.
first_word = company.split(" ")[0]

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(f"The index of the word coding: {company.index('Coding')}")
print(f"The index of the word coding: {company.find('Coding')}")

# 11. Replace the word coding in the string 'Coding For All' to Python.
new_company = company.replace("Coding", "Python")

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
replaced = new_company.replace("Everyone", "All")

# 13. Split the string 'Coding For All' using space as the separator (split()) .
replaced.split(" ")

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
strings = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
strings.split(",")

# 15. What is the character at index 0 in the string Coding For All.
replaced[0]

# 16. What is the last index of the string Coding For All.
replaced[-1]

# 17. What character is at index 10 in "Coding For All" string.
replaced[10]

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = "Python For Everyone"

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = "Coding For All"

# 20. Use index to determine the position of the first occurrence of C in Coding For A
cfa.index("C")
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
cfa.find("F")

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
cfa.rfind("l")

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
sentence = "You cannot end a sentence with because because because is a conjunction"
sentence.find("because")

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence:
sentence.rfind("because")

# 25. Slice out the phrase 'because because because' in the following sentence:
sentence[sentence.find("because") : sentence.rfind("because") + len("because")]

# 28. Does 'Coding For All' start with a substring Coding?
cfa.startswith("Coding")

# 29. Does 'Coding For All' end with a substring coding?
cfa.endswith("coding")

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
cfa = "   Coding For All      "
cfa.strip()

# 31. The following list contains the names of some of python libraries: Join the list with a hash with space string.
libariries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
("#").join(libariries)

# 33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\nBakary\t33\tSweden\tGothenburg")

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius**2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36. Make the following using string formatting methods:
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8**6}")
