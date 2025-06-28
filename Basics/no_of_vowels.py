n = str(input("Enter the String: "))
k = "".join(n.split())  
vowels = "aeiouAEIOU"
count=0
print("Vowels in the string:")
for i in k:
    if i in vowels:
        count+=1
print(f"No of vowels in {n}is : {count}" )