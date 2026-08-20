s=input("Enter string:")
vo="aeiou"
v=c=0
for ch in s:
   if ch.isalpha():
      if ch in vo:
      	v+=1
      else:
      	c+=1
print(f"vowels:{v}")
print(f"consonants:{c}")
