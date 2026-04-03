import random
import string

while True:
    print("\n1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    # 🔐 PASSWORD STRENGTH CHECKER
    if choice == '1':
        password = input("Enter your password: ")

        length = len(password)

        has_upper = False
        has_lower = False
        has_digit = False

        # check each character
        for ch in password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True

        # conditions for strength
        if length >= 8 and has_upper and has_lower and has_digit:
            print("Strong Password 💪")
        elif length >= 6:
            print("Medium Password 👍")
        else:
            print("Weak Password ❌")

    # 🔑 PASSWORD GENERATOR
    elif choice == '2':
        length = int(input("Enter desired password length: "))

        if length < 4:
            print("Password length should be at least 4")
            continue

        # characters to use
        all_chars = string.ascii_letters + string.digits

        password = ""

        for i in range(length):
            password += random.choice(all_chars)

        print("Generated Password:", password)

    # ❌ EXIT
    elif choice == '3':
        print("Program Ended.")
        break

    else:
        print("Invalid choice! Try again.")