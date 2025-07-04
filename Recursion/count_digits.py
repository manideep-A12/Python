def sum_d(n):
  c=0
  if(n==0):
    return 0
  return 1 + sum_d(n//10)
print(sum_d(123))