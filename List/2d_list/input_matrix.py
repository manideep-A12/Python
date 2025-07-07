n=int(input("Enter rows :"))
m=int(input("Enter col :"))
matrix=[]
for i in range(n):
  row=[]
  for j in range(m):
    k=int(input(f"Enter the element ({i},{j}) :"))
    row.append(k)
  matrix.append(row)
for row in matrix:
  print(row)
s,L_d,R_d=0,0,0
for i in range(n):
  for j in range(m):
    s+=matrix[i][j]
    if i==j:
      L_d+=matrix[i][j]
    if(i+j==n-1):
      R_d+=matrix[i][j]
for row in matrix:
  for element in row:
    print(element%2,end=" ")
  print()
    

print("Sum of elements in the matrix :",s)
print("Sum of Left_digonal elements in the matrix :",L_d)
print("Sum of Left_digonal elements in the matrix :",R_d)