def sub_string(s1,s2):
  for i in s1:
    for j in s2:
      if i in j:
        return "yes"
  return "no"
p = int(input())

for _ in range(p):
    s1 = input().strip()
    s2 = input().strip()
    print(sub_string(s1, s2))