n=[1,2,3,5,4,1]
m=sorted(n)
for i in range(1,len(m)-1):
  if m[i-1]==m[i]:
    print(f"first repeated Element : {m[i]}")
    break
else:
  print("No element is repeated")
  
