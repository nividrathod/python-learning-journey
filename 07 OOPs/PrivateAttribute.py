class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private attribute

    def show_marks(self):
        print("Marks:", self.__marks)


s1 = Student("Rahul", 90)

print(s1.name)         # Allowed
s1.show_marks()        # Allowed
# print(s1.__marks)    # AttributeError