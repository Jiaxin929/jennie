m = int(input('請輸入階層值M:'))
n = 1
i = 1
while(n < m):
        i = i + 1
        n = n * i
print("超過M為",m,"的最小階層N值為",i)