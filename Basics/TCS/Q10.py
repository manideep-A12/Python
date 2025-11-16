letters={}
a=1
for i in range(ord('A'),ord('Z')+1):
  letters[chr(i)]=a
  a+=1
key = 20
word = "HELLO WORLD"
for i in word:
  if i!=" ":
    print(letters[i]+key)
