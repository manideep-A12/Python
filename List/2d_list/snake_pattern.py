m=[[1,2,3],
   [1,2,3],
   [1,2,3]]

for i in range(3):
  for j in range(i + 1, 3):  
      m[i][j], m[j][i] = m[j][i], m[i][j]
for i in m:
  print(i)
