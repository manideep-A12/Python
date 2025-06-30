def insersation_sort(a):
  for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while j>=0 and temp<a[j]:
      a[j+1]=a[j]
      j-=1
    a[j+1]=temp
  return a
s=[2,7,4,5,8,9,3,1,6]
print(f"insersation_sort : {insersation_sort(s)}")
