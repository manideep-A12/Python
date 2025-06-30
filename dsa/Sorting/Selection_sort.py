a=[3,2,6,4,9,8,7]
for i in range(len(a)):
  min_ind=i
  for j in range(i+1,len(a)):
    if a[j]<a[min_ind]:
      min_ind=j
  a[i],a[min_ind]=a[min_ind],a[i]

print(a)