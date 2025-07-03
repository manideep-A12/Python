n=[1,2,3,4,5,3,4,3,2]
k,d=set(),set()
for i in n:
  if i in k:
    d.add(i)
  else:
    k.add(i)
print(d)
