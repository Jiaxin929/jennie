import math

a = float(input("請輸入路程公里數(Km):"))
if a < 1.5:
	print("所需車資為:",75)
else:
	if (a-1.5)<=0.25:
		print("所需車資為:",75+math.ceil((a-1.5)/0.25)*5)
	elif(a-1.5)>0.25:
		print("所需車資為:",75+math.ceil((a-1.5)/0.25)*5)