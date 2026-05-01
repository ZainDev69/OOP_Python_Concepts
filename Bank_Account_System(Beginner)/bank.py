from customer import Customer
from account import Account, SavingsAccount, CurrentAccount

class Bank:
    def __init__(self,name):
        self.name = name
        self.customers = {} # Using dictionary to access the data faster
        self.accounts = {}
        self.total_accounts_created = 0

    def add_customer(self,customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            print("Customer added successfully.")
        else:
            print("Customer already exists.")

    def remove_customer(self,customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print("Customer removed successfully.")
        else:
            print("Customer not found.")

    def find_customer(self,customer_id):
        return self.customers.get(customer_id)
    
    def create_account(self,customer_id,account_type,initial_deposit = 0, **kwargs):
        customer = self.find_customer(customer_id)
        if customer:
            account_number = f"{customer_id}-{self.total_accounts_created + 1}"
            if account_type == "Savings":
                interest_rate = kwargs.get("interest_rate",0.04)
                minimum_balance = kwargs.get("minimum_balance",1000)
                account = SavingsAccount(account_number,account_type,customer.name,interest_rate,minimum_balance)
                print(f"Savings account created successfully for {customer.name} with account number {account_number}.")

            elif account_type == "Current":
                overdraft_limit = kwargs.get("overdraft_limit",5000)
                account = CurrentAccount(account_number,account_type,customer.name,overdraft_limit)
                print(f"Current account created successfully for {customer.name} with account number {account_number}.")

            else:
                print("Invalid account type.")
                return  
        else:
            print("Customer not found. Cannot create account.")
        if initial_deposit > 0:
                    account.deposit(initial_deposit)
                    self.accounts[account_number] = account
                    self.customers[customer_id].add_account(account)
                    self.total_accounts_created += 1

    def find_account(self, account_number):
        return self.accounts.get(account_number)
    

    def delete_account(self,account_number):
        account = self.find_account(account_number)
        if not account:
            print("Account not found.")
            return
        
        if account.get_balance() > 0:
            print("Cannot delete account with a positive balance. Please withdraw the funds before deleting the account.")
            return
        

        del self.accounts[account_number]
        for customer in self.customers.values():
            if account in customer.accounts:
                customer.remove_account(account_number)
                break
            print("Account deleted successfully.")
            

    def accounts_by_customer(self,customer_id):
        customer = self.find_customer(customer_id)
        if customer:
            return customer.get_all_accounts()
        else:
            print("Customer not found.")
            return []
        

    def deposit(self,account_number,amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.") 


    def withdraw(self,account_number,amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.") 

    def transfer(self,from_account_number,to_account_number,amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            from_account.transfer(to_account,amount)
        else:
            print("One or both accounts not found.")


    def display_all_customers(self):
        for customer in self.customers.values():
            customer.__str__()

    def display_all_accounts(self):
        for account in self.accounts.values():
            account.__str__()

    def display_bank_summary(self):
        print(f"Bank Name: {self.name}")
        print(f"Total Customers: {len(self.customers)}")
        print(f"Total Accounts: {len(self.accounts)}")

    

    def __str__(self):
        return f"Bank Name: {self.name}, Total Customers: {len(self.customers)}, Total Accounts: {len(self.accounts)}"
    
        
    

