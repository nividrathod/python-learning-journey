class Account:

    def __init__(self,name,acc_num,balance):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def debit(self):
        amount = int(input("\nEnter amount you want to debit: "))
        if amount > self.balance:
            print("Not Sufficient Balance\n")
            return
        else:
            self.balance -= amount
            print("\nAmount Succefully Debited !!")

    def credit(self):
            amount = int(input("\nEnter amount you want to credit: "))
            self.balance += amount
            print("Amount Succefully Credited !!\n")

    def print_bal(self):
        print(f"\nAccount Holder Name: {self.name}\nAccount Number: {self.acc_num}\nCurrent Balance: {self.balance}")
        

ac1 = Account("Vishesh",111,1000)
ac2 = Account("Tanishk",222,15000)
ac3 = Account("Varrrun",333,20000)

ac1.print_bal()
ac1.debit()
ac1.print_bal()
ac1.credit()
ac1.print_bal()
