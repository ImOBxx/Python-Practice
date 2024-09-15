class Student:
    def __init__ (self, m, s, e, admo, sname):
        self.m = m
        self.s = s
        self.e = e
        self.admo = admo
        self.sname = sname

    def ctotal(self):
        return self.e + self.m + self.s

    def __str__(self):
        print()
        return (f"STUDENT DETAILS :- \n\n"
                f"The Student Name: {self.sname}\n"
                f"The Student Admission Number: {self.admo}\n\n"
                f"English Marks: {self.e}\n"
                f"Maths Marks: {self.m}\n"
                f"Science Marks: {self.s}\n\n"
                f"Total Marks:  {self.ctotal()}")

print()
print("Enter Student Details :- ")
print()
sname = input("Enter Student Name: ")
admo = input ("Enter Student Admission Number: ")
e = float (input("Enter English Marks: "))
m = float (input("Enter Maths Marks: "))
s = float (input ("Enter Science Marks: "))
print()

s1 = Student(m, s, e, admo, sname)
print(s1)
print()

    














