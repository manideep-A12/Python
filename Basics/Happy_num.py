n=16
while(n>10):
  sum=0
  while(n!=0):
    d=n%10
    sum+=(d**2)
    n//=10
  n=sum
print("Happy" if(sum==1) else "Not_happy")