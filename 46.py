dict1={}
p = int(input("請輸入處理方式(1)keys及values(2)items"))
n = int(input("請輸入筆數:"))
if p == 1:
	for i in range(n):
		a = str(input("請輸入獎牌名稱:"))
		b = int(input("請輸入獎牌數量:"))
		dict1[a]=b
		print(a,"牌得到",dict1.get(a),"面")
else:
	for i in range(n):
		a = str(input("請輸入獎牌名稱:"))
		b = int(input("請輸入獎牌數量:"))
		dict1[a]=b
		item1 = list(dict1.items())
	for key , value in item1:
		print("%s牌得到%d面"%(key,value))