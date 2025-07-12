# Create student class that takes name & marks of 3 students as arguments in constructor.
#then create a method to print the avarage.

class Student:
  def __init__(self,name: str, m1: int, m2: int, m3: int):
    self.name= name
    self.m1=m1
    self.m2=m2
    self.m3=m3
  def avarage(self):
    avg = (self.m1+self.m2+self.m3)/3
    return f"{avg} is the avarage of the  subjects"
s1=Student("Manideep",45,87,90)
print(s1.avarage())
