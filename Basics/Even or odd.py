# type one 
n=int(input("Enter the number :"))
if(n%2==0):
  print(f"{n} is even")
else:
  print(f"{n} is odd")


# type two(using bitwise and gate(&))
if(n&1==0):
  print(f"{n} is even")
else:
  print(f"{n} is odd")
