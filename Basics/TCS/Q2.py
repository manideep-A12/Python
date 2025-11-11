"""Problem Statement 

Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. 
Today he got one tricky question. 
The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. 
Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.

Constrains-
1<=N<=100

Example 1:
Input : 10  -> Integer

Output : 5    -> result- Integer

Explanation:
Binary representation of 10 is 1010. 
After toggling the bits(1010), will get 0101 which represents “5”. 
Hence output will print “5”."""

"""n= 10 
s=" "
k=bin(n)[2:]
for i in k:
  if i == "1":
    s+="0"
  else:
    s+="1"
print(int(s,2))"""
n= 10
k=n.bit_length()
s=(1<<k)-1
print(n^s)




  