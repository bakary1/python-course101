########################
## Day 11 - Functions
########################

## Exercises: Level 1

# 1. Declare a function add_two_numbers.
def add_two_numbers(num1, num2) -> int:
    return num1 + num2


# 2. Write a function called add_all_nums
def add_all_nums(values: list[int | float]) -> int | float:
    for item in values:
        if not isinstance(item, (int, float)):
            raise TypeError(f"The argument '{item}' is not a number")
    return sum(values)


# 3. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_temp(celsius: float) -> float:
    farenheit = (celsius * (9 / 5)) + 32
    return round(farenheit, 2)


convert_temp(32.2)


# 4. Write a function called check-season
def check_season(month: str) -> str:
    if month.lower() in ["december", "january", "february"]:
        return "Winter"
    elif month.lower() in ["march", "april", "may"]:
        return "spring"
    elif month.lower() in ["june", "july", "august"]:
        return "Summer"
    elif month.lower() in ["september", "october", "november"]:
        return "Autumn"
    else:
        return "Please enter a valid month"


# 5. Declare function called print_list
def print_list(lst: list[any]) -> None:
    for i in lst:
        print(i)


print_list(["hello", "test", 4, "nu"])


# 10. Declare a function named reverse_list.
def reverse_list(lst: list) -> list:
    reversed_list = []
    for idx in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[idx])
    return reversed_list


reverse_list([1, 2, 3])

## Exercises: Level 2


# 1. Declare a function named evens_and_odds
def evens_and_odds(number: int):
    if not isinstance(number, int):
        raise TypeError(f"{number} is not a valid input. Must be a positive integer")
    else:
        evens_num = []
        odds_num = []

        for num in range(number + 1):
            if num % 2 == 0:
                evens_num.append(num)
            else:
                odds_num.append(num)
        return f"The number of odds are {len(evens_num)}. The number of evens are {len(odds_num)}"


evens_and_odds(100)


# 2. Call your function is_empty,
def is_empty(item):
    if not item:
        return "The parameter is empty"
    else:
        return "The parameter is not empty"


is_empty(["s"])


# 4. Write a function called greet
def greet(name="Guest"):
    return f"Hello, {name}!"


# 5. show_args function
def show_args(**args):
    print(f"Received: {args}")


show_args(name="Bakary", age=35, jobbtitle="AI Engineer")

## Exercises: Level 3
