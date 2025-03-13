import sys
import random
import string

# Default values
length = 16
use_numbers = False
use_special = False
use_letters = False

def generate_password(length, use_numbers, use_special, use_letters):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # A-Z and a-z
    if use_numbers:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # Special characters

    if not characters:
        print("Error: You must select at least one option (-n, -s, -l).")
        return ""

    return ''.join(random.choice(characters) for _ in range(length))



for i, arg in enumerate(sys.argv[1:]):
    if arg == "-len" and i + 1 < len(sys.argv[1:]):
        try:
            length = int(sys.argv[i + 2])  # Convert next thing to an integer
        except ValueError:
            print("Error: Invalid length value.")
            sys.exit(1)
    elif "-n" in arg:
        use_numbers = True
    elif "-s" in arg:
        use_special = True
    elif "-l" in arg:
        use_letters = True

#default to all
if not (use_numbers or use_special or use_letters):
    use_numbers = use_special = use_letters = True

password = generate_password(length, use_numbers, use_special, use_letters)
print("Generated password:", password)