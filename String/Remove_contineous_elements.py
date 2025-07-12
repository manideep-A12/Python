n="abbcdaccdbb"
k=[]
k.append(n[0])
for i in range(1,len(n)):
  if n[i-1]!=n[i]:
    k.append(n[i])
print(*k)