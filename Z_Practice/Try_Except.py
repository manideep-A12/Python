m=int(input("Enter :"))
n=int(input("Enter :"))
try:
  div=m/n
  print(div)
except(ZeroDivisionError):
  print("denimator is zero")

