bp=int(input("Enter a basic pay:"))
da=0.2*bp
hra=0.5*bp
pf=0.11*bp
Grade=input("Enter grade of employee:")
if(Grade=="A"):
   allowance=1700
elif(Grade=="B"):
   allowance=1500
elif(Grade=="C"):
   allowance=1000
else:
   print("invalid")
np=bp+da+hra+allowance-pf
print("Net pay:",np)
[24bcs167@mepcolinux ex1]$cat grade.py 
mark=int(input("Enter a mark:"))
if(mark>90 and mark<=100):
   print("'O'Grade")
elif(mark>80 and mark<=90):
   print("'A+'Grade")
elif(mark>70 and mark<=80):
   print("'A'Grade")
elif(mark>60 and mark<=70):
   print("'B'Grade")
else:
   print("invalid grade")
