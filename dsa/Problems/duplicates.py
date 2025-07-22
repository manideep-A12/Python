a=[1,2,2,3,4,4,6,7,7]
i=0
for j in range(1,len(a)):
  if a[j]!=a[i]:
    i+=1
    a[i]=a[j]
print(a[:i+1])
