m=0
flag=0
n = 11
if(n == 1):
  flag = 1
  print("Not Prime")
for i in range(2,n):
  if(n % i == 0):
      print("Not Prime")
      flag=1
      break  
  
if (flag==0):
  print("Prime")