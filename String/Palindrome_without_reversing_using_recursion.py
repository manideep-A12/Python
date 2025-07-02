#checking given string is palindrome or not without reversing the string using recursion
def palindrome(s,st,e):
  if s[st]>=s[e]:
    return True
  if s[st]!=s[e]:
    return False
  return palindrome(s,st+1,e-1)
k="Madam".lower()
if palindrome(k,0,len(k)-1):
  print("yes")
else:
  print("no")

#checking given string is palindrome or not without reversing the string

n="madam".lower()
l,r=0,len(n)-1
while(l<r):
  if(n[l]!=n[r]):
    print("No")
    break
  l+=1
  r-=1
else:
  print("yes")