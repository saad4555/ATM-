# Simple ATM Program with 4-digit PIN

accounts = {}

def create_account():
    name = input("Apna naam enter karein: ")

    # 4 digit PIN check
    while True:
        pin = input("4 digit PIN set karein: ")
        if pin.isdigit() and len(pin) == 4:
            break
        else:
            print("❌ PIN sirf 4 digit number honi chahiye!")

    balance = int(input("Shuru ka balance enter karein: "))

    accounts[pin] = {
        "name": name,
        "balance": balance
    }

    print("✅ Account successfully create ho gaya!\n")

def check_balance(pin):
    print(f"💰 Apka current balance hai: {accounts[pin]['balance']} Rs\n")

def deposit(pin):
    amount = int(input("Deposit amount enter karein: "))
    accounts[pin]['balance'] += amount
    print("✅ Amount successfully deposit ho gaya!\n")

def withdraw(pin):
    amount = int(input("Withdraw amount enter karein: "))
    
    if amount > accounts[pin]['balance']:
        print("❌ Insufficient balance!\n")
    else:
        accounts[pin]['balance'] -= amount
        print("💵 Please collect your cash!\n")

def atm_menu():
    while True:
        print("===== ATM MENU =====")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Apna option select karein: ")

        if choice == "1":
            check_balance(user_pin)
        elif choice == "2":
            deposit(user_pin)
        elif choice == "3":
            withdraw(user_pin)
        elif choice == "4":
            print("🙏 ATM use karne ka shukriya!")
            break
        else:
            print("❌ Invalid option!\n")

# Main Program
print("===== WELCOME TO ATM =====")
print("1. Create Account")
print("2. Login")

option = input("Apna option select karein: ")

if option == "1":
    create_account()

# 4 digit PIN login check
user_pin = input("Apni 4 digit PIN enter karein: ")

if user_pin.isdigit() and len(user_pin) == 4 and user_pin in accounts:
    print(f"👋 Welcome {accounts[user_pin]['name']}!\n")
    atm_menu()
else:
    print("❌ Invalid PIN ya account exist nahi karta.")
