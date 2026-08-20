n=input("Enter String:")
l=n.split()
d=[]
i=len(l)-1
while(i>=0):
   d.append(l[i])
   i=i-1
   opt=''.join(d)
print(opt)
