s=int(input("enter the size of list :"))
if(s<0):
  print("Invalid array Size")
else:
  list_1=[]
  for i in range(s):
    k=input(f"Enter element {i+1} :")
    try:
      m=int(k)
      list_1.append(int(k))
    except(ValueError):
      print("invalid Array Element")
      break
  else:
    key=int(input("Enter the key value :"))
    c=0
    for i in list_1:
      if(i<key):
        c+=1
    if(c!=0):
      print(c)
    else:
      print("No such values below the given key value")
  
  
