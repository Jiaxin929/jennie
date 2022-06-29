sum = list(input("請輸入數字"))
sum.sort()
min=""
max=""
if len(sum) >= 8 or len(sum) <= 0:
    print("超出範圍")
else:
    for i in range(len(sum)):
        min += sum[i]
    sum.reverse()
    for i in range(len(sum)):
        max += sum[i]
    ans = int(max)-int(min)
    print("最大值數列與最小值數列差值為:",ans)