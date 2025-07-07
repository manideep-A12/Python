a=[1,0,2,0,3,0]
non_zeros=[x for x in a if x!=0]
zeros=[x for x in a if x ==0]
print(zeros+non_zeros)
