m="maalayalam"
for i in range(len(m)):
  k=m[:i]+m[i+1:]
  if k==k[::-1]:
    print(f"is a pallindrome : {k}")
    break


