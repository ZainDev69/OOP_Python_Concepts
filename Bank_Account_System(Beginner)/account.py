from datetime import datetime

class Account:
    def __init__(self,account_number,account_type,holder_name):
        self.account_number = account_number
        self.account_type = account_type
        self.holder_name = holder_name
        self.created_at = datetime.now()
        self.transaction_history = []
        self._balance = 0.0


    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")

        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self,target_account,amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            target_account.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to {target_account.account_number}")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def get_balance(self):
        return self._balance
    

    def show_transcation_history(self):
        for transaction in self.transaction_history:
            print(transaction)

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Created At: {self.created_at}")
        print(f"Balance: {self._balance}")


    def __str__(self):
        return f"Account Number: {self.account_number}, Account Type: {self.account_type}, Holder Name: {self.holder_name},Balance: {self._balance}"



class SavingsAccount(Account):
    def __init__(self,account_number,holder_name,interest_rate,minimum_balance):
        super().__init__(account_number,"Savings",holder_name)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance

    def calculate_interest(self):
        interest = self._balance * self.interest_rate
        return interest
    
    def add_interest(self):
        interest = self.calculate_interest()
        super().deposit(interest)  # Method overriding

    def withdraw(self,amount):
        if amount > 0 and amount (self.get_balance() - amount) >= self.minimum_balance:
            super().withdraw(amount)   # Method overriding
            
        else:
            print("Invalid withdrawal amount or insufficient funds.")



class CurrentAccount(Account):
    def __init__(self,account_number,holder_name,overdraft_limit):
        super().__init__(account_number,"Current",holder_name)
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        if amount > 0 and (self.get_balance() + self.overdraft_limit) >= amount:
            super().withdraw(amount)  # Method overriding
            self.deduct_transaction_fee()
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deduct_transaction_fee(self):
        fee = 5.0
        if self.__balance >= fee:
            self.__balance -= fee
            self.transaction_history.append(f"Deducted Transaction Fee: {fee}")
        else:
            print("Insufficient funds to deduct transaction fee.")


