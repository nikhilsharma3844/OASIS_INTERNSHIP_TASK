import random

# Define character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

def get_user_preferences():
    length = int(input("Enter the desired password length: "))

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_letters, use_numbers, use_symbols

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""

    if use_letters:
        character_pool += letters
    if use_numbers:
        character_pool += numbers
    if use_symbols:
        character_pool += symbols

    if character_pool == "":
        return "Error: You must select at least one character type."

    password = ""
    for _ in range(length):
        password += random.choice(character_pool)

    return password

def main():
    print("=== Random Password Generator ===")

    length, use_letters, use_numbers, use_symbols = get_user_preferences()
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
