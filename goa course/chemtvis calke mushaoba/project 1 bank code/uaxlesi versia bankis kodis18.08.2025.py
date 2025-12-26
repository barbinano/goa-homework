import time 
import sys 


def loading_screen_2(choice_option):
 for i in range(3):  
    for dots in range(4):  
        sys.stdout.write("\rLoading transaction history" + "." * dots + "   ") 
        
        time.sleep(0.5)  
        if i == 2 and dots == 3:
            if choice_option == "2":
                print("\r ")



         

def loading_screen_1(choice_option):
 for i in range(2):  
    for dots in range(4):  
        sys.stdout.write("\rLoading " + "." * dots + "   ")  
        
        time.sleep(0.5)  
        if i == 1 and dots == 3:
         

         if choice_option == "2":
           print("\rdeposit successful,")

        if i == 1 and dots == 3:

          if choice_option == "3":
             print("")
        if i == 1 and dots == 3:

         if choice_option == "4":
            print("")

        if i == 1  and dots == 3:


          if choice_option == "5":
            print("")  
        

        if i == 2 and dots == 3:

         if choice_option == "7":
            print("")

        

        




def loading_screen_0(choice_option):
 for i in range(2):  
    for dots in range(4):  
        sys.stdout.write("\rLoading" + "." * dots + "   ")  
        
        time.sleep(0.5)  
        if i == 1 and dots == 3:
         

         if choice_option == "1":
           print("")



def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def slow_input(prompt):
    slow_print(prompt)
    return input("")

exchange_rates = {
    "GEL": {"USD": 0.37, "EUR": 0.34},
    "USD": {"GEL": 2.7, "EUR": 0.92},
    "EUR": {"GEL": 2.95, "USD": 1.09}
}

accounts = {
    "saba": {"password": "1111", "balance": 30.0, "history": [], "currency": "GEL" },
    "gia": {"password": "2222", "balance": 20.0, "history": [], "currency": "USD"  },
    "admin": {"password": "admin", "balance": 0.0, "history": [], "currency": "GEL"} 

}



transaction_fee = 0.10



def convert(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    return amount * exchange_rates[from_currency][to_currency]

slow_print(" Welcome to goavalut")


while True:
    slow_print("\n1. Login")
    slow_print("2. Create Account")
    choice = slow_input("Choose option 1 or 2: ") 

    if choice == "1":  
        username = slow_input("Enter username: ")
        if username in accounts:
            password = slow_input("Enter password: ")
            loading_screen_0(choice)
            if password == accounts[username]["password"]:
                slow_print(" Welcome, " + username + ".\n")

                while True:
                    slow_print("\nWhat would you like to do?")
                    slow_print("1. Check balance")
                    slow_print("2. Deposit money")
                    slow_print("3. Withdraw money")
                    slow_print("4. Transfer money")
                    slow_print("5. Account settings")
                    slow_print("6. Log out")

                    if username == "admin":
                        slow_print("7. Admin view (see all accounts)")

                    bank_choice = slow_input("Choose option: ")

                    
                    if bank_choice == "1":
                        slow_print(f"Your balance is {accounts[username]['balance']:.2f} {accounts[username]['currency']}")

                    
                    elif bank_choice == "2":
                        amount = float(slow_input("Enter deposit amount: "))
                        dep_currency = slow_input("Enter currency (GEL/USD/EUR): ").upper()
                        if dep_currency not in exchange_rates:
                            slow_print("Unsupported currency.")
                            continue
                        if amount > transaction_fee:
                            loading_screen_1(bank_choice)
                            converted = convert(amount, dep_currency, accounts[username]['currency'])
                            accounts[username]['balance'] += (converted - transaction_fee)
                            slow_print(f" {amount} {dep_currency} converted to {converted:.2f} {accounts[username]['currency']}. Fee applied.")
                            accounts[username]["history"].append(f"{username} deposited {amount}{dep_currency} -> {converted:.2f}{accounts[username]['currency']}, fee {transaction_fee}{accounts[username]['currency']}")
                        else:
                            slow_print("Amount too small (must be larger than the fee).")

                    
                    elif bank_choice == "3":
                        amount = float(slow_input("Enter withdrawal amount: "))
                        total = amount + transaction_fee
                        if total <= accounts[username]['balance']:
                            accounts[username]['balance'] -=  total
                            loading_screen_1(bank_choice)
                            slow_print(f"Withdrawal successful! You took {amount} {accounts[username]['currency']}. Fee applied.")
                            accounts[username]["history"].append(f"{username} withdrew {amount}{accounts[username]['currency']}, fee {transaction_fee}{accounts[username]['currency']}")
                        else:
                            slow_print("Insufficient funds!")

                    
                    elif bank_choice == "4":
                        recipient = slow_input("Enter recipient username: ")
                        if recipient in accounts and recipient != username:
                            amount = float(slow_input("Enter transfer amount: "))   
                            total = amount + transaction_fee
                            if total <= accounts[username]['balance']:
                                accounts[username]['balance'] -= total
                                converted_amount = convert(amount,
                                                           accounts[username]['currency'],
                                                           accounts[recipient]['currency'])
                                accounts[recipient]['balance'] += converted_amount
                                loading_screen_1(bank_choice)
                                slow_print(f"Transfer successful! {amount} {accounts[username]['currency']} converted to {converted_amount:.2f} {accounts[recipient]['currency']}.")
                                accounts[username]["history"].append(f"{username} transferred {amount}{accounts[username]['currency']} -> {recipient} ({converted_amount:.2f}{accounts[recipient]['currency']}), fee {transaction_fee}{accounts[username]['currency']}")
                                accounts[recipient]['history'].append(f"{username} transferred {amount}{accounts[username]['currency']} -> {recipient} ({converted_amount:.2f}{accounts[recipient]['currency']}), fee {transaction_fee}{accounts[username]['currency']}")
                                
                            else:
                                slow_print("Insufficient funds!")
                        else:
                            slow_print("Invalid recipient.")

                    elif bank_choice == "5":
                        loading_screen_1(bank_choice)
                        while True:
                            slow_print("\nAccount Settings:")
                            slow_print("1. Change password")
                            slow_print("2. View transaction history")
                            slow_print("3. Delete account")
                            slow_print("4. Exit account settings")
                            settings_option = slow_input("Choose option 1-4: ")

                            if settings_option == "1":
                                new_pass = slow_input("Enter new password: ")
                                accounts[username]["password"] = new_pass
                                slow_print("Password changed successfully.")
                                


                            elif settings_option == "2":
                                loading_screen_2(settings_option)
                                slow_print("Transaction History:")

                                if username == "admin":
                                        
                                    for user, data in accounts.items():
                                        slow_print(f"\n{user}'s history:")
                                        if not data["history"]:
                                            slow_print(" - No transactions yet.")
                                        else:
                                         for entry in data["history"]:
                                                slow_print(" - " + entry)
                                else:
                                   
                                    if not accounts[username]["history"]:
                                     slow_print("No transactions yet.")
                                    else:
                                     for entry in accounts[username]["history"]:
                                            slow_print("- " + entry)

                            elif settings_option == "3":
                                confirm = slow_input("Are you sure you want to delete your account? (yes/no): ")
                                if confirm.lower() == "yes":
                                    del accounts[username]
                                    slow_print("Your account has been deleted.")
                                    break

                            elif settings_option == "4":
                                slow_print("Returning to menu...")
                                break
                            else:
                                slow_print("Invalid option. Please try again.")

                    elif bank_choice == "6":
                        slow_print("Goodbye, have a nice day")
                        break

                    elif bank_choice == "7" and username == "admin":
                        loading_screen_1(bank_choice)
                        slow_print("All accounts:")
                        for user, data in accounts.items():
                            slow_print(f"- {user}: {data['balance']:.2f} {data['currency']}")

                    else:
                        slow_print("Invalid option. Please try again.")
            else:
                slow_print("Wrong password.")
        else:
            slow_print("Username not found.")

    elif choice == "2":  
        new_user = slow_input("Choose a username: ")
        if new_user in accounts:
            slow_print("The username is already taken.")
        else:
            new_password = slow_input("Choose a password: ")
            new_currency = slow_input("Choose account currency (GEL/USD/EUR): ").upper()
            if new_currency not in exchange_rates:
                slow_print("Unsupported currency, defaulting to GEL.")
                new_currency = "GEL"
            accounts[new_user] = {"password": new_password, "balance": 0.0, "history": [], "currency": new_currency}
            slow_print(f"Account created successfully with currency {new_currency}.")

    else:
        slow_print("Invalid option. Please choose 1 or 2.")
