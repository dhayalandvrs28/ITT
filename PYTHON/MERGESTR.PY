n1=input("Enter String:")
n2=input("Enter String:")
opt=' '
i,j=0,0
while(i<len(n1) or j<len(n2)):
   if(i<len(n1)):
      opt+=n1[i]
      i+=1
   if(j<len(n2)):
      opt+=n2[j]
      j+=1
print(opt)
