n=int(input())
if(n<=0):
  print("Invalid List Size")
else:
  m=[]
  for i in range(n):
    k=input()
    if(k.isalpha()):
      m.append(k.lower())
    else:
      print("Invalid list Element")
  v='aeiou'
  c=0
  for i in m:
    if i not in v:
      c+=1
  print(f"Count : {c if c>0 else "No consonants found"}")

