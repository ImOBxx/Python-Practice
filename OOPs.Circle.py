class Circle:
    def __init__(self, r):
        self.r = r

    def areacalc(self):
        return 3.14 * r * r
    
    def circumcalc(self):
        return 2 * 3.14 * r
    
    def __str__(self):
        return (f"RECTANGLE'S COMPUTATIONS :- \n"
                f"Area Of The Circle: {round(self.areacalc(), 2)}\n"
                f"Circumference Of The Circle: {self.circumcalc()}\n")

print()
print("RECTANGLE :- ")
print()   
r = int (input ("Enter Radius: "))
print()
s1 = Circle(r)
print(s1)