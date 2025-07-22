d={'a':1,'b':2,'c':3}
k=""
n=0
for i,j in d.items():
  if j>n:
    n=j
    k=i
print(n,"  ",k)