year = int(input("請輸入西元年"))
dict1 =["猴","雞","狗","豬","鼠","牛","虎","兔","龍","蛇","馬","羊"]
m = year % 12
print("你的生肖為{}".format(dict1[m]))