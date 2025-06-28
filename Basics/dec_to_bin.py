d=int(input("Enter the decimal num :"))
binn=""
while(d!=0):
  s=d%2
  binn+=str(s)
  d//=2
print(f"Binary value is: {binn}")
