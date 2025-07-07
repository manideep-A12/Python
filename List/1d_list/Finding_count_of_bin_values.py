def count_1(a):
  l,r=0,len(a)-1
  while(l<r):
    mid=(l+r)//2
    if(a[mid]==1):
      l=mid+1
    else:
      r=mid-1
  return r
a=[1,1,1,1,0,0,0]
print(count_1(a))