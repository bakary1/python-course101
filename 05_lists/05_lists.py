########################
## Day 5 - Lists
########################

## Exercises: Level 1

# 1 Declare an empty list
empty = []

# 2. Declare a list with more than 5 items
fruits = ["apple", "banana", "kiwi", "mango", "orange", "pineapple"]

# 3. Find the length of your list
print(f"Number of elements in the list: {len(fruits)}")

# 4. Get the first item, the middle item and the last item of the list
print(f"First item: {fruits[0]}")
print(f"Middle item: {fruits[len(fruits) // 2]}")
print(f"Last item: {fruits[-1]}")

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Bakary", 34, 170, "Single", "Gothenburg"]

# 6. Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 8. Print the number of companies in the list
print(f"Number of companies: {len(it_companies)}")

# 9. Print the first, middle and last company
print(f"First company: {it_companies[0]}")
print(f"Middel company: {it_companies[len(it_companies) // 2]}")
print(f"Last company: {it_companies[-1]}")

# 10: Print the list after modifying one of the companies
it_companies[6] = "Nvidia"

# 11. Add an IT company to it_companies
it_companies.append("Microsoft")

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Spotify")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# 14. Join the it_companies with a string '#;  '
"# ".join(it_companies)

# 15. Check if a certain company exists in the it_companies list.
if "Spotify" in it_companies:
    print("Spotify is in the list")
else:
    print("Spotify is not in the list")

# 16. Sort the list using sort() method
sorted_companies = sorted(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
it_companies[:3]

# 19. Slice out the last 3 companies from the list
it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
it_companies[len(it_companies) // 2]

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)

# 23. Remove the last IT company from the list
it_companies.pop(-1)

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

front_end.extend(back_end)

# 27. After joining the lists in question..
full_stack = front_end.copy()

full_stack.insert(5, "SQL")

###########################
## Exercises: Level 2
###########################

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2. Sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = sorted_ages[0]
max_age = sorted_ages[-1]

# 3. Add the min and max ages again
sorted_ages.append(min_age)
sorted_ages.append(max_age)
sorted_ages.sort()

# 4. Find the median age (one middle item or two middle items divided by two)
item1 = sorted_ages[len(sorted_ages) // 2]
item2 = sorted_ages[len(sorted_ages) // 2 - 1]

# 5. Find the average age (sum of all items divided by their number )
average = sum(sorted_ages) / len(sorted_ages)

# 6. Find the range of the ages (max minus min)
range_ages = sorted_ages[-1] - sorted_ages[0]

# 7. Compare the value of (min - average) and (max - average), use abs() method
sorted_ages[0] - average

# 8. Country list
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

mid_country1 = countries[len(countries) // 2]
mid_country2 = countries[len(countries) // 2 - 1]

# 9. Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_part1 = countries[len(countries) // 2 :]
countries_part2 = countries[: len(countries) // 2]

# 10. Unpack the first three countries and the rest as scandic countries.
countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
china, russia, usa, *scandic_countries = countries
