def vowels(s):
  return sum(1 for c in s if c.lower() in "aeiou")
print(vowels("Hello world"))