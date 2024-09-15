class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"Person's Details :- \n\n" 
                f"Name Of The Person: {self.name}\n\n"
                f"Age Of The Person: {self.age}\n")
    

print()
print("Enter Person's Details. ")
print()
name = input ("Enter Name Of The Person: ")
age = int (input ("Enter Age Of The Person: "))
print()
s1 = Person(name, age)
print(s1)
