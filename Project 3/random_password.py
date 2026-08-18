import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print(" Random Password Generator ")

    try:
        length = int(input("Enter your password length: "))

        if length < 1:
            print("Error: Password length does not match.")
            return

        password = generate_password(length)

        print("\n Generated Password :")
        print(password)

    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()