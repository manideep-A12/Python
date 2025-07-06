s="mourya"
l=0
for i in range(6):
  for j in range(6):
    if(i==j):
        print(s[l],end=" ")
        l+=1
        break
    else:
      print(" ",end=" ")
  print()