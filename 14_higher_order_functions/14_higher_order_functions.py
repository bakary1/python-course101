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


# 12. Declare a function called categorize_countries that returns a list of countries with some common pattern

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


def categorize_countries(country_lst: list[str]) -> list[str]:
    return list(filter(lambda country: "land" in country, country_lst))


categorize_countries(countries)


# 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
from collections import Counter


def returning_dict(country_lst: list[str]) -> dict[str, int]:

    starting_letters = []

    for country in country_lst:
        starting_letters.append(country[0])

    letter_count = Counter(starting_letters)

    return dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))


returning_dict(countries)
