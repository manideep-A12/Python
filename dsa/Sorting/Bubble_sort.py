def Bubble_sort(a):
  k=len(a)
  for i in range(k):
    for j in range(0,k-i-1):
      if(a[j+1]<a[j]):
        a[j],a[j+1]=a[j+1],a[j]
  return a
m=[7,6,5,4,3,2,1]
print(Bubble_sort(m))