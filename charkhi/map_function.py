####################################
## Map function
####################################

## Exercises

## map(func, iterable) -> map object

# example 1
list_of_fruits = ["apple", "orange", "kiwi", "banana"]

list(map(str.upper, list_of_fruits))

# example 2
numbers = [1, 2, 3, 4, 5]

list(map(float, numbers))

# example 3:  map with custom function


# squared function
def squared(num):
    return num**2


list(map(squared, numbers))

# using the lambda function
list(map(lambda x: x**2, numbers))


# clean data

raw_names = ["  Alice  ", "BOB", " ChArLiE"]

clean_names = list(map(lambda x: x.strip().title(), raw_names))
