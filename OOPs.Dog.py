class Dog:
    def __init__(self, n, b):
        self.n = n
        self.b = b
    
    def __str__(self):
        return (f"DOG INFO :- \n\n"
                f"Name Of The Dog: {self.n}\n\n"
                f"Breed Of The Dog: {self.b}\n")

print()
print("ENTER DOG INFO :-")
print()
n = input ("Enter Name Of The Dog: ")
print()
b = input ("Enter Breed Of The Dog: ")
print()

s1 = Dog(n, b)
print(s1)