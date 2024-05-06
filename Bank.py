class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.AllBankAccount = []
        self.total_bank_balance = self.total_balance()
        self.is_loan = True

    def add_account(self, account):
        self.AllBankAccount.append(account)

    def total_balance(self):
        self.total_bank_balance = 0  
        for account in self.AllBankAccount:
            self.total_bank_balance += account.inital_balance
        return self.total_bank_balance
    
    def login_user(self,email,password):
        for account in self.AllBankAccount:
            if email == account.email and password == account.password:
                return account
        return 
