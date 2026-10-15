class Grandfather:
    def show_grandfather(self):
        print("I am Grandfather")

class Father(Grandfather):
    def show_father(self):
        print("I am Father")

class Child(Father):
    def show_child(self):
        print("I am Child")

obj = Child()

obj.show_grandfather()
obj.show_father()
obj.show_child()