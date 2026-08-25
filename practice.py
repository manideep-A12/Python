k=int(input("Enter a number :"))
try:
  c=100/k
  print(c)
except ZeroDivisionError:
  print("Enter value other then 0 !!!!")