n=input("Enter String:")
l=n.split()
d=[]
i=0
while(i<len(l)):
   if(i%2==0):
      d.append(l[i])
   else:
      d.append(l[i][::-1])
   i+=1
opt=' '.join(d)
print("Actual string:",n)
print("Generated String:",opt)
