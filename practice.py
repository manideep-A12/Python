#sum of colns

n=[[1,2,3],
   [3,4,6],
   [7,8,9]]
print("Sum of colns :",end=" ")
for i in range(len(n[0])):
  sum=0
  for j in range(len(n)):
    sum+=n[i][j]
  print(sum,end=" ")


