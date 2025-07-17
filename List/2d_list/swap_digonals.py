'''n=4
c=[]
for i in range(n):
  r=[]
  for j in range(n):
    k=int(input("Entetr the element :"))
    r.append(k)
  c.append(r)
for r in c:
  print(r)
'''
m=[[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 8, 9, 7],
[6, 5, 4, 3]]
k=0
while(k<4):
  m[k][0],m[k][2]=m[k][2],m[k][0]
  k+=1
for i in m:
  print(i)
print(len(m[0]))
