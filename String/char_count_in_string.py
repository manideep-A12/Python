#count fequency of character in given String
s="Manasa"
f={}
for n in s:
  if n in f:
    f[n]+=1
  else:
    f[n]=1
max_char=max(f, key=f.get)
print(f)
print("Most frequent char", max_char ,":",f[max_char])

