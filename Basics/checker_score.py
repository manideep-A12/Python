def score_checker(a):
  Results={}
  d = int(input("Enter the NUmber of students : "))
  for _ in range(d):
    name=str(input("Enter the name :"))
    score=int(input("Enter the score :"))
    Results[name]=score
  print(Results)
