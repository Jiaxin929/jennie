n = int(input("小狗有可能跑到的幾個地方:"))
for i in range(1,n+1):
	k = int(input("跑到離家幾公里的地方:"))
	if k%9==0 or k%11==0:
		print("第",i,"個點",k)
	else:
		print(0)