n=5
#left triange
print("Left Triangle")
for i in range(1,n+1):
  print("* "*i)

print() #its optional, i used it for get a line space in the output 

#Right Triange
print("Right triangle")
for i in range(1,n+1):
  print("  "*(n-i),"* "*i) #double space

print()

#Pyramid
print("Pyramid")
for i in range(1,n+1):
  print(" "*(n-i),"* "*i) #single space

print()

#inverted Pyramid
print("inverted Pyramid")
for i in range(n,0,-1):
  print(" "*(n-i),"* "*i) #single space

print()

#diamond
print("diamond")
for i in range(1,n+1):
  print(" "*(n-i),"* "*i) #single space
for i in range(n-1,0,-1):
  print(" "*(n-i),"* "*i) #single space

print()

#Left Half diamond
print("Left Half diamond")
for i in range(1,n+1):
  print("* "*i)
for i in range(n-1,0,-1):
  print("* "*i)

print()


#Right Half Dimond
print("Right Half Dimond")
for i in range(1,n+1):
  print("  "*(n-i),"* "*i) 
for i in range(n-1,0,-1):
  print("  "*(n-i),"* "*i) 