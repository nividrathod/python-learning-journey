class College:

    def __init__(self,name):
        self.name = name

    @staticmethod       # staticmethod: Methods that don't use the self parameter (works at class level)
    def welcome():
        print("Welcome Everyone")

c1 = College("Varrrun")
print("Name:",c1.name)
c1.welcome()