while True:
	a = input("請輸入整數數列(end 結束)")
	if a == "end":
		print("結束")
		break
	else:
		x = (a[::-1])
		if x == a:
			print(a[::-1])