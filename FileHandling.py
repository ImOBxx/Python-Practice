"""with open ('1. This is Text File.txt', 'r') as f:
     f.write('Test')"""

with open('1. This is Text File.txt', 'r') as rf:
     with open('test_copy.txt', 'w') as wf:
          for line in rf:
               wf.write(line)
          
          
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     """f.write('Test')
     f.seek(0)
     f.write('R')"""
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     """size_to_read = 10

     f_contents = f.read(size_to_read)
     print(f_contents, end = ' ')

     f.seek(0)

     f_contents = f.read(size_to_read)
     print(f_contents)"""

     """while len (f_contents) > 0:
       print(f_contents, end = '*')
       f_contents = f.read(size_to_read)"""

     """f_contents = f.readline(1)
     print(f_contents, end = ' ')

     f_contents = f.readline(1)
     print(f_contents, end = ' ')"""


     

