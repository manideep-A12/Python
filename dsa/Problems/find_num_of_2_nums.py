#find the 2 numbers where their sum is equal to the target
#if we use 2 pointers approch it will be having best time complicity 
list2=[1,2,3,4,5,6,7,8,9,10]
list1=sorted(list2)
target=10
left_pointer=0
right_pointer=len(list1)-1
while(left_pointer<right_pointer):
  c_sum=list1[left_pointer]+list1[right_pointer]
  if c_sum==target:
    print(f"{list1[left_pointer]} + {list1[right_pointer]} = {target}")
    right_pointer-=1
    left_pointer+=1
  elif c_sum>target:
    right_pointer-=1
  else:
    left_pointer+=1
  
