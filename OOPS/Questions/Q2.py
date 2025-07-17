class Anagrams:
  def __init__(self,str1,str2):
    self.str1=str1
    self.str2=str2
  
  def anag(self):
    s=sorted(self.str1)
    k=sorted(self.str2)

    return s,k
sl=Anagrams("live","evil")
m=sl.anag()

