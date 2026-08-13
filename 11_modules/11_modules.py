########################
## Day 13 - Modules
########################

## Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
from random import randint, choice
import string


def random_user_id() -> str:
    """Generate a random 6-character user ID made of alternating digits and letters.

    Returns:
        A 6-character string alternating one random digit
        and one random ASCII letter, three times
    """
    user_id = ""
    possible_chars = string.ascii_letters

    for _ in range(3):
        number = str(randint(0, 9))
        character = choice(possible_chars)
        user_id += number
        user_id += character

    return user_id


random_user_id()

# alt solution from Claude

# def random_user_id() -> str:
#     """Generate a random 6-character user ID made of alternating digits and letters.

#     Returns:
#         A 6-character string alternating one random digit and one random
#         ASCII letter, three times.
#     """
#     possible_chars = string.ascii_letters

#     parts = [str(randint(0, 9)) + choice(possible_chars) for _ in range(3)]
#     return "".join(parts)

# 2. Modify the previous task.
