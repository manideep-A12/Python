r,c=3,3
m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
max=m[0][0]
min=m[0][0]
for i in range(r):
  for j in range(c):
    if m[i][j]>max:
      max=m[i][j]
    if m[i][j]<min:
      min=min[i][j]
print(f"Max of matrix : {max}")
print(f"Min of matrix : {min}")