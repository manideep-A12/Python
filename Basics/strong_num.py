def fact(n):
  if n==1:
    return 1
  return n*fact(n-1)
n=145
sum=0
for i in str(n):
  sum+=fact(int(i))
print(sum)
