class Student:

    def __init__(self,name,phy,che,math):
        self.name = name
        self.phy = phy
        self.che = che
        self.math = math

    def avg(self):
        avg = (self.phy + self.che + self.math)/3
        print("Average marks of",self.name,":",avg)

s1 = Student("Pranjal",87,79,95)
s2 = Student("Yash",75,84,91)
s3 = Student("Varrrun",84,93,82)

s1.avg()
s2.avg()
s3.avg()