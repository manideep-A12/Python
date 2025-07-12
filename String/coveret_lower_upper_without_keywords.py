n="aAbBcC"
for i in n:
  if(ord(i)>=97):
    m=chr(ord(i)-32)
    print(m,end="")
  else:
    m=chr(ord(i)+32)
    print(m,end="")
