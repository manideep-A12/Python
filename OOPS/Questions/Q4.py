class Triangle:
  def __init__(self,n):
    self.s=n
    
  #left triangle // Method
  def left_triangle(self):
    print("left_triangle")
    for i in range(1,self.s+1):
      print("* "*i)
  
  #right triangle //Method
  def right_triangle(self):
    print("right_triangle")
    for i in range(1,self.s+1):
      print("  "*(self.s-i),"* "*i)

  #pyramid //Method
  def pyramid(self):
    print("pyramid")
    for i in range(1,self.s+1):
      print(" "*(self.s-i),"* "*i)
  
  #reverse pyramid //Method
  def reverse_pyramid(self):
    print("reverse pyramid")
    for i in range(self.s,0,-1):
      print(" "*(self.s-i),"* "*i)
  
  #diamond //Method
  def diamond(self):
    print("diamond")
    for i in range(1,self.s+1):
      print(" "*(self.s-i),"* "*i)
    for i in range(self.s-1,0,-1):
      print(" "*(self.s-i),"* "*i)
  
  def right_half_diamond(self):
    print("right_half_diamond")
    for i in range(1,self.s+1):
      print("  "*(self.s-i),"* "*i)
    for i in range(self.s-1,0,-1):
      print("  "*(self.s-i),"* "*i)
  
  def left_half_diamond(self):
    print("left_half_diamond")
    for i in range(1,self.s+1):
      print("* "*i)
    for i in range(self.s-1,0,-1):
      print("* "*i)


t1=Triangle(5)
t1.left_triangle()
print()
t1.pyramid()
print()
t1.reverse_pyramid()
print()
t1.diamond()
print()
t1.right_half_diamond()
print()
t1.left_half_diamond()