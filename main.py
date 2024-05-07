from Bank import Bank
from users import Admin, Bank_account


mama_bank = Bank("Mama")


def user_menu(user_account):

    while True:
        print("\nUser Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Take Loan")
        print("5. Transfer Money")
        print("6. Transaction History")
        print("7. Profile")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            user_account.deposit(amount,mama_bank)
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            user_account.withdraw(amount, mama_bank)
        elif choice == 3:
            user_account.check_balance()
        elif choice == 4:
            amount = int(input("Enter the loan amount: "))
            user_account.take_loan(amount, mama_bank)
        elif choice == 5:
            amount = int(input("Enter the amount to transfer: "))
            account_number = input("Enter the User account number: ")
            user_account.transfer_amount(amount, account_number, mama_bank)
        elif choice == 6:
            user_account.all_transaction_history()
        elif choice == 7:
            user_account.profile()
        elif choice == 8:
            print("Exiting user menu.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


admin_data = {"username": "admin", "password": 1234}


def admin_menu():
    name = input("Enter Your Name: ")
    password = int(input("Enter Your password: "))

    if name == admin_data["username"] and password == admin_data["password"]:
        admin = Admin(name, password)
        print("Authentication successful.")
        while True:
            print("\nAdmin Menu:")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. View All Accounts")
            print("4. Check Bank Balance")
            print("5. View Total Loan Amount")
            print("6. Turn Loan Feature On/Off")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                user_name = input("Enter user's name: ")
                user_email = input("Enter user's email: ")
                user_address = input("Enter user's address: ")
                account_type = input("Enter account type: ")
                password = input("Enter account password: ")
                account = Bank_account(
                    user_name, user_email, user_address, account_type, password)
                admin.create_account(account, mama_bank)
            elif choice == 2:
                account_number = input("Enter the account number to delete: ")
                admin.delete_account(account_number, mama_bank)
            elif choice == 3:
                admin.view_all_account(mama_bank)
            elif choice == 4:
                admin.bank_balance(mama_bank)
            elif choice == 5:
                total_loan = admin.loan_amount(mama_bank)
                print(f"Total Loan Amount: {total_loan}")
            elif choice == 6:
                print("You want to On Loan Feature or Off Loan Feature")
                onoff = input("Enter Your Choice (On/Off): ")
                if onoff.lower() == 'on':
                    mama_bank.is_loan = True
                    print("Loan Feature is Available Now !!")
                elif onoff.lower() == 'off':
                    mama_bank.is_loan = False
                    print("Loan Feature is Not Available Now !!")
            elif choice == 7:
                print("Exiting admin menu.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
    else:
        print("Authentication failed. Invalid username or password.")


while True:
    print(f"Welcome To {mama_bank.name}")
    print("1. User Account")
    print("2. Admin Account")
    print("3. Exiting Bank")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1. Login User Account")
        print("2. Create User Account")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            email = input("Enter Your email: ")
            password = input("Enter Your password: ")
            user = mama_bank.login_user(email, password)
            if user:
                user_menu(user)
            else:
                print("Authentication failed. Invalid username or password.")

        elif choice == 2:
            name = input("Enter Your Name: ")
            email = input("Enter Your email: ")
            address = input("Enter Your address: ")
            account_type = input("Enter Your Account Type (savings/current): ")
            password = password = input("Enter Your password: ")
            if account_type.lower() == 'savings' or account_type.lower() == 'current':
                user_account = Bank_account(
                    name, email, address, account_type, password)
                mama_bank.add_account(user_account)
                user_menu(user_account)
            else:
                print("You enter a wrong account type !!. Please try Again")
        else:
            print("Invalid choice. Please choose a valid option.")
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        print("Exiting The Bank.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
