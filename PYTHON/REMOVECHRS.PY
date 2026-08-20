n=input("Enter String:")
l=[]
for x in n:
   if x not in l:
      l.append(x)
      opt=''.join(l)
print(opt)
