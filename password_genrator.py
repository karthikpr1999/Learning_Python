import string
import secrets

# Define character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_characters = letters + digits + symbols

# Ask for length
try:
    length = int(input("Enter the length of the password: "))
    if length < 4:
        raise ValueError("Password length must be at least 4 for strength.")
except ValueError as e:
    print("Invalid input:", e)
    exit()

# Ensure at least one of each type
password = [
    secrets.choice(letters),
    secrets.choice(digits),
    secrets.choice(symbols),
]

# Fill the rest randomly
password += [secrets.choice(all_characters) for _ in range(length - 3)]

# Shuffle to avoid predictable order
secrets.SystemRandom().shuffle(password)

# Join into a string
password = ''.join(password)

print("Your secure password is:", password)
