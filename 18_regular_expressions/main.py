import re

test_string = "1234abc4567abc2920ABC"
a = "\tHello"
print(a)

# finditer method
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)


# findall() - returns all matches
matches = pattern.findall(test_string)

for match in matches:
    print(match)

# match() - return the first macth
match = pattern.match(test_string)
print(match)

# search() - returns first match
match = pattern.search(test_string)
print(match)

# recommended to use finditer most of the time
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

# group, star, end, span methods
for match in matches:
    print(match.span(), match.start(), match.end())
    print(match.group())

# meta charachters
# . ^ $ * + ? {} [ ] \ | ( )

# . Finds any charachter (except new line character)
# ^ Starts with "^hello"
# $ Ends with "worlds$"
# * Zero or more occurances "aix*"
# + One ore more occurances "aix+"
# { } Exatcly the specified number of occurances "al{2}"
#  [] A set of charachters "[a-m]"
# \ Special sequence (or escape special characters) "\d"
# | Either or "falls|stays"
# ( ) Capture and group

# Examples "."
test_string = "1234kdjndndo."
pattern = re.compile(r"^123")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

####################
# Part 2
####################
test_string = "hello 123_ heyho hohey"
pattern = re.compile(r"[0-9]")
matches = pattern.finditer(test_string)

for match in matches:
    print(matches)
