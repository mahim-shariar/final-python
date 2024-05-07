class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.AllBankAccount = []
        self.total_bank_balance = 0
        self.is_loan = True

    def add_account(self, account):
        self.AllBankAccount.append(account)

    
    def login_user(self,email,password):
        for account in self.AllBankAccount:
            if email == account.email and password == account.password:
                return account
        return 
