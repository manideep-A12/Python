n="abcadcbaef"
s={}
for i in n:
  if i in s:
    s[i]+=1
  else:
    s[i]=1
print(s)
for k,v in s.items():
  if v==1:
    print(k)
    break
