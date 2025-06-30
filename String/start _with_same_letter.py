a="banana is a fruit. bird is flying"
s="b"
c=0
m=a.split()
for i in m:
  if(i[0]==s):
    c=c+1
    print(i)
print("Count of the words :",c)