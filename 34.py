a = int(input("請輸入一正整數(11<=a<=1000):"))
if a%2==0 and a%11==0 and a%5!=0 and a%7!=0:
	print(a,"為新公倍數?:"+"Yes")
else:
	print(a,"為新公倍數?:"+"No")