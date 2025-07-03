n=100
for i in range(n+1):
  s=i
  while(i>10):
    sum=0
    while(i!=0):
      d=i%10
      sum+=(d**2)
      i//=10
    i=sum
  if(sum==1):
    print(s)
