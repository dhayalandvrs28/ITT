num=int(input("Enter a num:"))
sum=0
temp=num
pow=len(str(num))
while(temp!=0):
   digit=temp%10
   sum+=(digit**pow)
   temp//=10
if(sum==num):
   print("Armstrong num")
else:
   print("Not a Armstrong num")
