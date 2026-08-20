s=input("Enter String:")
result=""
for ele in s:
   if(ele>='a' and ele<='z'):
      result+=chr(ord(ele)-32)
   else:
      result+=ele
print(result)
