def sum_digit(n):
  return sum(int(i) for i in str(n))
def xyz(n,r):
  fsum = sum_digit(n)
  ssum=fsum*r
  while ssum > 10 :
    ssum=sum_digit(ssum)
  return ssum
print(xyz(99,3))
  
