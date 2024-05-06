from abc import ABC
import uuid


class Users(ABC):
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address


class Bank_account(Users):
    def __init__(self, name, email, address, account_type,password) -> None:
        super().__init__(name, email, address)
        self.account_type = account_type
        self.inital_balance = 0
        self.account_number = str(uuid.uuid4())[:6]
        self.all_transaction = []
        self.loan_count = 0
        self.loan_amount = 0
        self.password = password

    def profile(self):
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Account Type:{self.account_type}")
        print(f"Account Number:{self.account_number}")
    

    def deposit(self, amount):
        if amount > 0:
            self.inital_balance += amount
            self.all_transaction.append(f"You are deposit :{amount}")

            print("Deposit successful")

        else:
            print("Invalid number")

    def withdraw(self, amount, bank):
        if amount > 0 and amount < self.inital_balance:
            if bank.total_bank_balance > amount:
                self.inital_balance -= amount
                self.all_transaction.append(f"You are Wtihdraw :{amount}")
                print("withdraw successful")
            else:
                print("bank is bankrupt")
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        print(f"Your Total Balance: {self.inital_balance}")

    def take_loan(self, amount, bank):
        if amount > 0 and self.loan_count <= 2 and bank.total_bank_balance > amount and bank.is_loan == True: 
            self.inital_balance += amount
            self.loan_count += 1
            self.all_transaction.append(f"You Take loan from the bank: {amount} ")
            self.loan_amount += amount
            print("Take Loan successful")

        else:
            print("You can take loan higst two time !!")

    def transfer_amount(self, amount, account_number, bank):
        for account in bank.AllBankAccount:
            if account.account_number == account_number and amount <= self.inital_balance:
                account.inital_balance += amount
                self.inital_balance -= amount
                self.all_transaction.append(f"Transferred {amount} to account {account_number}")
                account.all_transaction.append(f"Recived {amount} from account {account_number}")
                print("Transfer successful!")
                return
        print("Account does not exist.!!")
    
    def all_transaction_history(self):
        for trans in self.all_transaction:
            print("--------------------ALL Transaction----------------------")
            print(f"{trans}\n")
            print("---------------------------------------------------------")


class Admin:
    def __init__(self, name,password) -> None:
        self.password = password
        self.name = name

    def create_account(self, account, bank):
        bank.add_account(account)
        print("create an account successfully")

    def delete_account(self, account_number, bank):
        for account in bank.AllBankAccount:
            if account.account_number == account_number:
                bank.AllBankAccount.remove(account)
                print("Account deleted successfully")
                return
        print("Account not found")

    def view_all_account(self, bank):
        print("--------------View All Account------------------")
        for account in bank.AllBankAccount:
            print(f"Name:{account.name}, Email:{account.email}, Address:{account.address}, Account Type: {account.account_type}, Account Number: {account.account_number}")
        print("------------------------------------------------")

    def bank_balance(self, bank):
        print(f"{bank.name} Total Balance is : {bank.total_balance()}")
    
    def loan_amount(self,bank):
        total_loan = 0
        for account in bank.AllBankAccount:
            total_loan += account.inital_balance
        return total_loan
    

