n=int(input("ENter :"))
is_prime=False
for i in range(2,int(n**0.5)+1):
  if(n%i==0):
    is_prime=True
    break
if is_prime:
  print("prime")
else:
  print("non-prime")