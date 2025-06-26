n=int(input("Enter the value :"))
count=0
for i in range(2,n):
  if(n%i==0):
    count=count+1
if(count==0):
  print("Prime Number")
else:
  print("Non-Prime Number")


# prime using Functions
def Prime_no(n):
  count=0
  for i in range(2,n):
    if(n%i==0):
      count=count+1
  return count

n=int(input("Enter the number :"))
k=Prime_no(n)
if(k==0):
  print("Prime Number")
else:
  print("Non-Prime Number")