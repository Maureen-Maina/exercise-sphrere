#bank account program 
import datetime
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = datetime.datetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            print("Invalid deposit amount")
            return None

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        elif amount > self.balance:
            print("Insufficient balance")
            return None
        else:
            print("Invalid withdrawal amount")
            return None

    def check_balance(self):
        print(f"Current balance: ksh{self.balance:.2f}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Account Opening: {self.date_of_opening}")
        print(f"Current Balance: ksh{self.balance:.2f}")

account = BankAccount("123456789", "Maureen Maina")

account.deposit(100000)
account.check_balance()

withdrawal_amount = float(input("Enter withdrawal amount: "))
withdrawn = account.withdraw(withdrawal_amount)
if withdrawn:
    print(f"Withdrawn amount: ksh{withdrawn:.2f}")
    account.check_balance()
    
account.customer_details()
    
