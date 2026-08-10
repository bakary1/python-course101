########################
## Day 6 - Tuples
########################

## Exercises: Level 1

# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
len(it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Netflix", "Nvidia"])

# 4. Remove one of the companies from the set it_companies
it_companies.remove("Twitter")

# 5. What is the difference between remove and discard
## No error if the item is not in the set

## Exercises: Level 2

# 1. Join A and B
A.union(B)

# 2. Find A intersection B
A.intersection(B)

# 3. Is A subset of B
A.issubset(B)

# 4. Are A and B disjoint sets
A.isdisjoint(B)

# 5. Join A with B and B with A
A.union(B)
B.union(A)

# 6. What is the symmetric difference between A and B
A.symmetric_difference(B)

# 7. Delete the sets completely
del A, B
del it_companies

## Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
len(age)
len(set(age))

# 3. split the sentence
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split(" "))

print(f"There are {len(unique_words)} unique words in the set.")
