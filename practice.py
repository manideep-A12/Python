instruction=["Choose a number Between 0 to 99 ","Add 5 to the number","Multiply with 50","add 365","add your age(range between (0-99))","Enter your overall value"]
while True:
  for i in range(5):
    print(f"Step {i+1}:{instruction[i]}")
    k=input(f"Enter ok if step {i+1} completed :")
    if k=='ok':
      continue
    else:
      print("Thammudu leniponive enter cheyyamakuu !!")
      break
  else:
    s=int(input("Enter your overall value :"))
    n=str(s)
    r=int(n[-2:])-15
    l=int(n[:-2])-6
    print("Your age is :",r)
    print("Your Chosen number is :",l)
    exit()
