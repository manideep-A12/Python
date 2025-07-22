n=5
k=1
for i in range(1,n+1):
  print(" "*(n-i),end=" ")
  for j in range(i):
    print(f"{k} ",end="")
    k+=1
  print()