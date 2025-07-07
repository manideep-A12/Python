m=[[1,2,3],
   [1,2,3],
   [1,2,3]]
for i in range(3):
  for j in range(3):
    s=0
    e=len(m[i])-1
    while s<e:
      m[i][s],m[j][e]=m[i][e],m[j][s]
      s+=1
      e-=1
for i in m:
  print(i)