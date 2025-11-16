letters={}
k="1"
for i in range(ord('A'),ord('Z')+1):
  letters[chr(i)]=k
  k+='1'
n="101101110"
s=n.split('0')
for i,j in letters.items():
  for char in s:
    if char==j:
      print(i,end="") 
