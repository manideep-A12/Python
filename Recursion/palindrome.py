def palin(s,l,r):
  if(l>=r):
    return True
  if(s[l]!=s[r]):
    return False
  return palin(s,l+1,r-1)
print(palin("madam",0,len("madam")-1)) 
