from itertools import combinations
s="mmmaannniideeeppp"
for i in range(len(s)):
  for c in combinations(s,i):
    print("".join(c))

