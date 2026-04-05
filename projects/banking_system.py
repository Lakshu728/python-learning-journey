# Simple Banking System

balance = 0

# Function to check balance
def check_balance():
    print("Your current balance is:", balance)

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

# Main menu loop
while True:
    print("\n===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            check_balance()

        case 2:
            deposit()

        case 3:
            withdraw()

        case 4:
            print("Thank you for using bank system!")
            break

        case _:
            print("Invalid choice! Try again.")