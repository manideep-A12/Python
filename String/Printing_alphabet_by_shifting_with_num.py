n="D"
i=2
h=ord(n)
sum=i+h
if('a'<= n <='z' and sum > ord('z')):
  sum=sum-26
elif('A'<= n <='Z' and sum > ord('Z')):
  sum-=26
print(chr(sum))
