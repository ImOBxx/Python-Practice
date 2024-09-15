class Rectangle:
    def __init__(self, h, w):
        self.w = w
        self.h = h

    def areacalc(self):
        return self.h * self.w
    
    def pericalc(self):
        return 2 * (self.h + self.w)

    def __str__(self):
        return (f"Rectangle Dimensions :- \n"
                f"The Area Of The Rectangle Is: {self.areacalc()}\n"
                f"The Perimemter Of A Rectangle Is: {self.pericalc()}\n")

print()
print("Rectangle :- ")
print()   
h = int (input ("Enter Height Of The Rectangle: "))
w = int (input ("Enter Width Of The Rectangel: "))

s1 = Rectangle(h, w)
print(s1)

