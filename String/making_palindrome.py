m="maalayalam"
for i in range(len(m)):
  k=m[:i]+m[i+1:]
  if k==k[::-1]:
    print(f"{k} is a pallindrome")
    break
else:
    print("There is no palindrome word")
