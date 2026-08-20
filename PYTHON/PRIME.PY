num=int(input("Enter a num:"))
if(num<2):
   print("not a prime")
else:
   for i in range(2,int(num**0.5)+1):
      if(num%i==0):
	 print("Not a prime no")
	 break
      else:
	 print("Prime no")
