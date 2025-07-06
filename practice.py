n=[1,2,6,7,5,-1,0]
m=set(x for x in n if x>0)
i=1
while True:
  if i not in m:
    print(i)
    break
  i+=1
