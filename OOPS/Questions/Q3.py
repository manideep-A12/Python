class Solution:
  def __init__(self,a):
    self.a=a
  def dublicates(self):
    d,u=[],[]
    for i in self.a:
      if i in u:
        d.append(i)
      else:
        u.append(i)
    return d
s1=Solution([1,2,3,4,2,3])
m=s1.dublicates()
print(m)