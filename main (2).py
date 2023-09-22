
class BankAccount:
    def __init__(self, acc_num, acc_holder, acc_bal):
        self.__account_number = acc_num
        self.__account_holder = acc_holder
        self.__account_balance = acc_bal

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account balance: {self.__account_balance}")


# Create a new bank account with initial balance of 1000
my_account = BankAccount("1234", "John Doe", 1000)

# Deposit 500 into the account
my_account.deposit(500)

# Withdraw 200 from the account
my_account.withdraw(200)

# Display the current balance
my_account.display_balance()
