n=int(input("Enter the value :"))
sum=0
for i in range(1,n):
  if(n%i==0):
    sum+=i
print(f"sum of factors : {sum}")
if(sum==n):
  print(f"{n} is a perfect number")
else:
  print(f"{n} is not a perfect number")
