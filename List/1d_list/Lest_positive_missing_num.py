l=[3,7,-1,8,9,10]
m=set(x for x in l if x > 0)
i=1
while True:
  if i not in m:
    print(i)
    break
  i+=1