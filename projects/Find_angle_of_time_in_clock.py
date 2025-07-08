n=input("Enter the Time :")
k=n.split(":")
h,m=int(k[0]),int(k[1])
Angle=(30*h+(m/2))-6*m
if(Angle<0):
  a=360+Angle
  print(f"The angle of {n} is {int(a)} Degrees")
else:
  print(f"The angle of {n} is {int(Angle)} Degrees")

