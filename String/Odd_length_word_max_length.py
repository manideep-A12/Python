s="Hello world good morning team"
k=s.split()
max=""
for i in k:
  if(len(i)%2==1):
    if(len(max)<len(i)):
      max=i
print(max)
