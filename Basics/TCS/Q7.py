n=3
m=3
k=max(n,m)
c=0
num=2
p=[]
while len(p)<k:
  for i in range (2,num):
    if num%i==0:
      break
  else: 
    p.append(num)
  num+=1
print(p)
print(p[n-1]+p[m-1]-1)
