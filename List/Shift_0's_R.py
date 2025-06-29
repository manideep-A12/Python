n=[2,4,3,0,8,0,7,0,6,7,0,0,5,5]
#[1,7,4,5,0,0]
j=0
for i in range(len(n)):
  if n[i]!=0:
    n[j]=n[i]
    j+=1
while(j<len(n)):
  n[j]=0
  j+=1
print(n)