import random
import string

def generate_password(length):
    """
    Generate a random password with the given length.

    Parameters:
    length (int): The length of the password to generate.

    Returns:
    str: A random password.
    """
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print(f"Generated password: {password}")