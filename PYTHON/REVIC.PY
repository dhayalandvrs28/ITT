n=input("Enter String:")
l=n.split()
d=[]
i=0
while(i<len(l)):
   d.append(l[i][::-1])
   i+=1
   opt=''.join(d)
print(opt)
