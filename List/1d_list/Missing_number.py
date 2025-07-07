n=int(input("Enter the no of elements :"))
m=[]
for i in range(n):
  k=int(input(f"Enter {i+1}:"))
  m.append(k)
s=sum(m)
n_sum=n*(n+1)//2
print("Missing Element :",n_sum-s)


#using binary search concept
def missing(a):
  l,r=0,len(a)-1
  while(l<r):
    mid=(l+r)//2
    if(a[mid]!=mid):
      r=mid
    else:
      l=mid+1
  return l
print(missing([0,1,3,4,5]))