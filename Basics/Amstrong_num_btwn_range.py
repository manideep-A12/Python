for i in range(5000):
  m=i
  k=len(str(i))
  sum=0
  while(i!=0):
    sum+=((i%10)**k)
    i//=10
  if(m==sum):
    print(m)
