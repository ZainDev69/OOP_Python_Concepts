"""
Bank Account System
Customer Module 
"""


from datetime import datetime
class Customer: 
    def __init__(self,customer_id,name,email,phone,address,date_of_birth):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.date_of_birth = date_of_birth
        self.created__at = datetime.now()
        self.is_active = True
        self.accounts = []

    def add_account(self,account):
        self.accounts.append(account)

    def remove_account(self,account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                break
            else:
                print("Account not found.")

    def get_account(self,account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

        else: 
            print("Account not found.")

    def get_all_accounts(self):
        return self.accounts

    def get_total_balance(self):
        for account in self.accounts:
            total_balance += account.balance
            return total_balance

    

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Account Numbers: {self.account}")

    
    def display_accounts_summary(self):
        for account in self.accounts:
            if self.accounts.length > 0:
                print(f"Account Number: {account.account_number}, Balance: {account.balance}")
            else:
                print("No accounts found for this customer.")


    



    def update_email(self,new_email):
        self.email = new_email

    def update_phone(self,new_phone):
        self.phone = new_phone

    def update_address(self,new_address):
        self.address = new_address

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Date of Birth: {self.date_of_birth}"


