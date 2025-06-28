n=[4,8,6,7,4,2,1]
min_val=n[0]
max_val=0
for i in range(len(n)):
  if n[i]>max_val:
    max_val=n[i]
  if n[i]<min_val:
    min_val=n[i]
print(f"maximum value in {n} is {max_val}")
print(f"minimum value in {n} is {min_val}")
