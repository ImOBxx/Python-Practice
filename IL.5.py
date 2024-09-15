print()
s1 = input ("Enter String 1: ")
print()
s2 = input ("Enter String 2: ")
print()
x1 = s1.replace(" ", "").lower()
x2 = s2.replace(" ", "").lower()
a = sorted(x1) == sorted(x2)
print("The String's Are Anagrams: ", a) 
print()


