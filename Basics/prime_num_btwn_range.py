n=int(input("ENter the N value :"))
print(f"All primes from 1,{n} :",end=" ")
for i in range(1,n+1):
  c=0
  for k in range(2,i):
    if(i%k==0):
      c+=1
      break
  if(c==0):
    print(i,end=" ")

