n="Manideep"
s=list(n.lower())
for i in range(len(n)):
  for j in range(len(n)-i-1):
    if(s[j+1]<s[j]):
      s[j+1],s[j]=s[j],s[j+1]
print("".join(s))

  
  