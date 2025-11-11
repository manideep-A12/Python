def altchar(s):
  c=0
  for i in range(1,len(s)):
    if s[i]==s[i-1]:
      c+=1
  return c
  
p=int(input())
for _ in range(p):
  s=input()
  print(altchar(s))