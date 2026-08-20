n=input("Enter String:")
n1=n2=opt=''
for x in n:
   if(x.isalpha()):
      n1+=x
   else:
      n2+=x
for x in sorted(n1):
   opt+=x
for x in sorted(n2):
   opt+=x
print(opt)
