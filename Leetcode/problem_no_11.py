def max_area(height: list[int]) -> int:
  l=0
  r=len(height)-1
  max_area=0
  while(l<r):
    Height=min(height[l],height[r])
    width=r-l
    area=Height*width
    max_area=max(max_area,area)
    if height[l]<height[r]:
      l+=1
    else:
      r-=1
  return max_area
print(max_area([1,8,6,2,5,4,8,3,7]))
     

