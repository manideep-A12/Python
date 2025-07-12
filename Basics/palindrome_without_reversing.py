n="kambk"
l,r=0,len(n)-1
while(l<r):
  if(n[l]!=n[r]):
    print("Not a palindrome")
    break
  l+=1
  r-=1
else:
  print("palindrome")