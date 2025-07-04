def rev_list(a,l,r):
  if(l>r):
    return
  else:
    t=a[l]
    a[l]=a[r]
    a[r]=t
    l+=1
    r-=1
    rev_list(a,l,r)
  return a
a=[1,2,3,4,5]
l=0
r=len(a)-1
print(rev_list(a,l,r))