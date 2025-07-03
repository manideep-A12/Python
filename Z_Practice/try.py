l=[1,-1,3,7,8,0,2,5,-6]
k=sorted(l)
j=0
for i in range(max(k)):
  if(k[j]>0):
    if(k[j]!=i):
      print(i)
      break
  j+=1