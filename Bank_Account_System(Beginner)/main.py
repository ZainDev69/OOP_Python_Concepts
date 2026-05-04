from customer import Customer
from bank import Bank
from getpass import getpass


def main():
    bank = Bank("State Bank of Pakistan")


    while True:
        print("-------------Login to the State Bank of Pakistan----------------")
        user_name = input("Username: ")
        user_pass = getpass("Password: ")        
        if user_name == "admin" and user_pass == "1234":    
            print("Login successful!")
            break    
        else:
            print("Invalid credentials. Try again.")




    while True:

        print("\n-------------Welcome to the State Bank of Pakistan----------------")
        print("1. Add New Customer")
        print("2. Remove Customer")
        print("3. View Customer Details")
        print("4. Create New Account (Savings/Current)")
        print("5.Delete Account")
        print("6. Deposit Money")
        print("7. Withdraw Money")
        print("8. Transfer Money")
        print("9. Check Account Balance")
        print("10. Show Transaction History")
        print("11. Show Customer's Accounts")
        print("12. Display All Customers")
        print("13. Display All Accounts")
        print("14. Bank Summary (Total Funds, Counts)")
        print("15. Add Interest (Savings only)")
        print("0. Exit")

        option = input("Please select an option: ")

        if option == "1": 
            customer_id = input("Enter customer ID: ")
            if not customer_id:
                print("Customer ID cannot be empty. Please try again.")
                continue
            name = input("Enter customer name: ")
            if not name:
                print("Customer name cannot be empty. Please try again.")
                continue
            address = input("Enter customer address: ")
            if not address:
                print("Customer address cannot be empty. Please try again.")
                continue
            phone = input("Enter customer phone: ")
            if not phone:
                print("Customer phone cannot be empty. Please try again.")
                continue

            email = input("Enter customer email: ")
            if not email:
                print("Customer email cannot be empty. Please try again.")
                continue
            date_of_birth = input("Enter customer date of birth (YYYY-MM-DD): ")
            if not date_of_birth:
                print("Customer date of birth cannot be empty. Please try again.")
                continue
            customer = Customer(customer_id,name, address, phone,email, date_of_birth)
            bank.add_customer(customer)
            print("----Customer added successfully.----")
            print(f"Customer ID: {customer.customer_id},\n Name: {customer.name},\n Address: {customer.address},\n Phone: {customer.phone}, \n Email: {customer.email}, \n Date of Birth: {customer.date_of_birth}")

        elif option == "2":
            customer_id = input("Enter customer ID to remove: ")
            bank.remove_customer(customer_id)

        elif option == "3":
            customer_id = input("Enter customer ID to view details: ")
            bank.find_customer(customer_id)

        elif option == "4":
            customer_id = input("Enter customer ID to create account for: ")
            account_type = input("Enter account type (Savings/Current): ")
            if account_type == "Savings":
                interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
                minimum_balance = float(input("Enter minimum balance: "))
                bank.create_account(customer_id, account_type, interest_rate=interest_rate, minimum_balance=minimum_balance)
                print("----Savings account created successfully.----")
                print(f"Customer ID: {customer_id}, Account Type: {account_type}, Interest Rate: {interest_rate}, Minimum Balance: {minimum_balance}")
            elif account_type == "Current":
                overdraft_limit = float(input("Enter overdraft limit: "))
                bank.create_account(customer_id, account_type, overdraft_limit=overdraft_limit)
                print("----Current account created successfully.----")
                print(f"Customer ID: {customer_id}, Account Type: {account_type}, Overdraft Limit: {overdraft_limit}")

        elif option == "5":
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)

        elif option == "6":
            account_number = int(input("Enter account number to deposit into: "))
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)

        elif option == "7":
            account_number = int(input("Enter account number to withdraw from: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif option == "8":
            from_account = int(input("Enter source account number: "))
            to_account = int(input("Enter destination account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(from_account, to_account, amount)

        elif option == "9":
            bank.display_all_customers()

        elif option == "10":
            bank.display_all_accounts()
    

        elif option == "0":
            print("Thank you for using the State Bank of Pakistan. Goodbye!")
            break
    
        else: 
            print("Invalid option. Please try again.")



    



if __name__ == "__main__":
    main()

    