n=input("Enter your DOB :")
data=n.split("-")
date={"sunday":0,"monday":1,"Tuesday":2,"Wednesday":3,"thursday":4,"friday":5,"saterday":6}
month={"01":0,"02":3,"03":3,"04":6,"05":1,"06":4,"07":6,"08":2,"09":5,"10":0,"11":3,"12":5}
d_val=int(data[0]) #date value
m_val=month[(data[1])] # month value
s1=data[2]
s1_val=s1[:2]
year=int(s1_val)*100
s2_val=int(s1[2:])
l_years=s2_val//4
year_val=s2_val+l_years
def century(year):
  p={0:6,100:4,200:2,300:0}
  v=1600
  dif=(year-v)%400
  return p[(dif//100)*100]
c_val=century(year)
year_val=s2_val+l_years+c_val #year_value
dob_val=d_val+m_val+year_val
ur_day=[k for k, v in date.items() if v == (dob_val%7)]
print(f"You are Born on {ur_day[0]}")