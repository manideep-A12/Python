def Fizzbuzz(n):
  if n % 3 == 0 and n%5 == 0:
    print("FizzBuzz")
  elif(n % 3 == 0):
    print("Buzz")
  elif(n % 5 == 0):
    print("Fuzz")
  else:
    print(n)
m = 15
for i in range(1,m+1):
  Fizzbuzz(i)
  

  



