n=input("Enter String:")
opt=''
for x in n:
   if x.isalpha():
      opt+=x
      prev=x
   else:
      opt+=chr(ord(prev)+int(x))
print(opt)
