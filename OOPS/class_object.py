class Student:
  name="Student"
  def __init__(self,name: str=None, marks: int=0):
    if name is not None:
      self.name=name
    else:
      self.name=Student.name
    self.marks=marks
  def get_name_marks(self):
    print(f"{self.marks}, Scored by {self.name}")


s1=Student(marks=87)
s1.get_name_marks()
