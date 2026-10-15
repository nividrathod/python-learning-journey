class Bank:
    def __init__(self):
        self.balance = 5000

    def __withdraw(self, amount):  # Private method
        self.balance -= amount
        print("Remaining balance:", self.balance)

    def withdraw_money(self, amount):
        self.__withdraw(amount)


b1 = Bank()

b1.withdraw_money(1000)  # Allowed
# b1.__withdraw(1000)    # AttributeError