import time
import random


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def slow_input(prompt):
    slow_print(prompt)
    return input("")

# Step 1: Store account information 
accounts = {
    "saba": {"password": "1111", "balance": 30.0, "history": [],},
    "gia": {"password": "2222", "balance": 20.0, "history": [], },
    "admin": {"password": "admin", "balance": 0.0, "history": [],}  # special admin account
}

transaction_fee = 0.10

slow_print(" Welcome to group 2 Bank ")

#loging in or creating an account
while True:
    slow_print("\n1. Login")
    slow_print("2. Create Account")
    choice = slow_input("Choose option   1 or 2: ")

    if choice == "1":  # LOGIN
        username = slow_input("Enter username: ")
        if username in accounts:
            password = slow_input("Enter password: ")
            if password == accounts[username]["password"]:
                slow_print("Login successful! Welcome, " + username + ".\n")

                # Banking menu
                while True:
                    slow_print("\nWhat would you like to do?")
                    slow_print("1. Check balance")
                    slow_print("2. Deposit money")
                    slow_print("3. Withdraw money")
                    slow_print("4. Transfer money")
                    slow_print("5. Create credit card")
                    slow_print("6. account settings")
                    slow_print("7. Log out")

                    # admin-only option
                    if username == "admin":
                        slow_print("8. Admin view (see all accounts)")

                    bank_choice = slow_input("Choose option: ")

                    if bank_choice == "1":
                        slow_print("Your balance is ₾" + str(accounts[username]['balance']))

                    elif bank_choice == "2":  # Deposit
                        amount = float(slow_input("Enter the deposit amount: "))
                        if amount > transaction_fee:
                            accounts[username]['balance'] += (amount - transaction_fee)
                            accounts[username]['history'].append(f"Deposited ₾{amount} (-₾{transaction_fee} fee)")
                            slow_print("Deposit successful! Fee applied.")
                        else:
                            slow_print("Amount too small (must be larger than the fee).")

                    elif bank_choice == "3":  # Withdraw
                        amount = float(slow_input("Enter withdrawal amount: "))
                        total = amount + transaction_fee
                        if total <= accounts[username]['balance']:
                            accounts[username]['balance'] -= total
                            accounts[username]['history'].append(f"Withdrew ₾{amount} (-₾{transaction_fee} fee)")
                            slow_print("Withdrawal successful! Fee applied.")
                        else:
                            slow_print("Insufficient funds!")

                    elif bank_choice == "4":  # Transfer
                        recipient = slow_input("Enter recipient username: ")
                        if recipient in accounts and recipient != username:
                            amount = float(slow_input("Enter transfer amount: "))
                            total = amount + transaction_fee
                            if total <= accounts[username]['balance']:
                                accounts[username]['balance'] -= total
                                accounts[recipient]['balance'] += amount
                                accounts[username]['history'].append(
                                    f"Transferred ₾{amount} to {recipient} (-₾{transaction_fee} fee)")
                                accounts[recipient]['history'].append(f"Received ₾{amount} from {username}")
                                slow_print("Transfer successful! Fee applied.")
                            else:
                                slow_print("Insufficient funds!")
                        else:
                     
                           slow_print("Invalid recipient.")
                     

                    elif bank_choice == "5":  # Credit card creation
                        if accounts[username]["card"]:
                            slow_print("You already have a card: " + accounts[username]["card"]["number"])
                        else:
                            card_number = str(random.randint(1000_0000_0000_0000, 9999_9999_9999_9999))
                            pin = str(random.randint(1000, 9999))
                            accounts[username]["card"] = {"number": card_number, "pin": pin}
                            slow_print("Credit card created!")
                            slow_print("Card Number: " + card_number)
                            slow_print("PIN: " + pin)
                    if bank_choice== "6":
                        while True:
                            slow_print("\n choose options 1-4")
                            slow_print("1. Change password")
                            
                            slow_print("3. Delete account")
                            slow_print("4. exit account settings")
                            account_settings_option=slow_input("choose option 1-4")


                            if account_settings_option == "1":  # Change password
                              new_pass = slow_input("Enter new password: ")
                              accounts[username]["password"] = new_pass
                              slow_print("Password changed successfully.")

                        
                            elif account_settings_option== "2":  # Transaction history
                             slow_print("Your transaction history:")
                             if accounts[username]['history']:
                              for hist in accounts[username]['history']:
                                slow_print(" - " + hist)
                             else:
                                 slow_print("No transactions yet.")

                            elif account_settings_option == "3":  # Delete account
                             confirm = slow_input("Are you sure you want to delete your account? (yes/no): ")
                             if confirm.lower() == "yes":
                                del accounts[username]
                                slow_print("Your account has been deleted.")

                            elif account_settings_option == "4":
                                slow_print("returning to menu ")
                                break


                




                    elif bank_choice == "7":
                        slow_print("Goodbye, have a nice day")
                        break

                    

                    elif bank_choice == "8" and username == "admin":  # Admin view
                        slow_print("All accounts:")
                        for user, data in accounts.items():
                            slow_print(f"- {user}: ₾{data['balance']}")
                    
                    else:
                        slow_print("Invalid option. Please try again.")
            else:
                slow_print("Wrong password.")
        else:
            slow_print("Username not found.")

    elif choice == "2":  # Creating an account1
        new_user = slow_input("Choose a username: ")
        if new_user in accounts:
            slow_print("The username is already taken.")
        else:
            new_password = slow_input("Choose a password: ")
            accounts[new_user] = {"password": new_password, "balance": 0.0, "history": [], "card": None}
            slow_print("Account created successfully")

    else:
        slow_print("Invalid option. Please choose 1 or 2.")




 