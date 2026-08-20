num=int(input("Enter a num:"))
temp=num
sum=0
while(temp>0):
   rem=temp%10
   sum+=rem
   temp//=10
   multiple=num/sum
   harshad=multiple*sum
if(harshad==num):
   print("Harshad num")
else:
   print("Not a harshad num")
