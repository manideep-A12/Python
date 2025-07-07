n=[2,7,11,3,6]
for i in range(1,len(n)):
  if n[i-1]+n[i]==9:
    print(i-1,i) 