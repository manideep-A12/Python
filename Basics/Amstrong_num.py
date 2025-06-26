n=int(input("Enter the number :"))
s=0
temp=n
while(n!=0):
  r=n%10
  s+=(r**3)
  n//=10
if(temp==s):
  print(f"{temp} is a amstrong number")
else:
  print(f"{temp} is not a amstrong number")
