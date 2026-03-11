#Banking System Simulation

def bank():
    print("-------BANK----------")
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")

class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"Balance = {self._balance}")
    
    def deposit(self):
        amount = int(input("enter the amount to deposit :"))
        self._balance += amount
        print(f"Deposit successful --- {amount}, updated balance --- {self._balance}")
    
    def withdraw(self):
        amount = int(input("enter the amount to withdraw :"))
        if amount > self._balance:
            print("Insufficient balance!!")
        else:
            self._balance -= amount
            print(f"Withdrawal successful --- {amount}, updated balance --- {self._balance}")

class SavingsAccount(Account):  # inheritance
    
    def calculate_interest(self):
        interest_rate = 0.05  # 5%
        interest = self._balance * interest_rate
        print("Interest is : ", interest)

class CurrentAccount(Account):
    def withdraw(self):  # polymorphism
        amount = int(input("enter the amount to withdraw :"))
        overdraft = 1000
        if amount <= self._balance + overdraft:
            self._balance -= amount
            print(f"Withdrawal successful --- {amount}, updated balance --- {self._balance}")
        else:
            print("Insufficient balance!!")
    
class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__account = {}

    def create_account(self, id, holder_name, type):
        if type == "savings":
            new_acc = SavingsAccount(id, holder_name)
        elif type == "current":
            new_acc = CurrentAccount(id, holder_name)
        self.__account[id] = new_acc
        print("Account created...")
        return new_acc
    
    def get_acc(self, id):
        if id not in self.__account:
            print("Account not found")
            return None
        else:
            acc = self.__account[id]
            print(f"ID: {acc.id}\nHolder name: {acc.holder_name}")
            return acc


bank_obj = Bank("MyBank", "Mumbai")

while True:
    bank()
    choice = int(input("enter your choice : "))
    if choice == 1:
        acc_type = input("enter acc type (savings/current): ")
        id = input("enter id: ")
        name = input("enter holder name: ")
        account = bank_obj.create_account(id, name, acc_type)
    elif choice == 2:
        id = input("enter account id: ")
        account = bank_obj.get_acc(id)
        if account:
            account.deposit()
    elif choice == 3:
        id = input("enter account id: ")
        account = bank_obj.get_acc(id)
        if account:
            account.withdraw()
    elif choice == 4:
        id = input("enter account id: ")
        account = bank_obj.get_acc(id)
        if account:
            account.check_balance()
    elif choice == 5:
        print("logged out...")
        break
    else:
        print("Invalid choice!!!")