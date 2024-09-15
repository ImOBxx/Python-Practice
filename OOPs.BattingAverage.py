class Batsman:
    def __init__(self, bcode, bname, inn, no, runs):
        self.bcode = bcode
        self.bname = bname
        self.inn = inn
        self.no = no
        self.runs = runs

    def calcavg(self):
        return ((self.runs) / (self.inn - self.no))
    
    def __str__(self):
        return (f"The Batsman Statistics :- \n\n"
                f"Batsman Name: {self.bname}\n"
                f"Batsman BarCode Number: {self.bcode}\n\n"
                f"Batsman Innings Played: {self.inn}\n"
                f"Batsman NotOut Inninhgs Played: {self.no}\n"
                f"Batsman Total Runs Scored: {self.runs}\n\n"
                f"Batsman Batting Average: {round(self.calcavg(), 2)}\n\n")
    


print()
print("Enter Batsman Details :- ")
print()
bcode = int (input ("Enter Batsman BarCode Number: "))
bname = input("Enter Batsman Name: ")
inn = int (input ("Enter Number Of Innings Played: "))
no = int (input ("Enter Number Of Not Out Innings Played: "))
runs = int (input("Enter Runs Scored By The Batsman: "))
print()


s1 = Batsman(bcode, bname, inn, no, runs)
print(s1)
