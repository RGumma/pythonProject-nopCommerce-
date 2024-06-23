class Student:
    school = 'Telesco'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg_marks(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a static method")

s1=Student(62,75,95)
print(s1.avg_marks())
print(Student.get_school())
print(Student.info())
