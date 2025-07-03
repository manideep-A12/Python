n=int(input("Enter the number of applictions :"))
all_A=[]
count=0
for i in range(n):
  k=str(input(f"Enter the application {i+1}:"))
  all_A.append(k.lower())
vowel="aeiou"
for x in all_A:
  if x not in vowel:
    count+=1
print(count)