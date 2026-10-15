class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Yash")
print(s1.name)

del s1.name     # Deletes Attribute or Object
print(s1.name)