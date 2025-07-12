p="am in class but not able to concentrate"
count=0
for i in range(len(p)):
  if i==0 and p[i]!=" " or p[i]!=" " and p[i-1]==" ":
    count+=1
print(count)