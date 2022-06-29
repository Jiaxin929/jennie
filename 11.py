md = input("請輸入月及日(格式為0929):")
month = int(md[0:2])
day = int(md[2:5])
if (month == 1 and 21<=day<=31) or (month == 2 and 1<=day<=18):
    print("星座為:水瓶座")
elif (month == 2 and 19<=day<=29) or (month == 3 and 1<=day<=20):
    print("星座為:雙魚座")
elif (month == 3 and 21<=day<=31) or (month == 4 and 1<=day<=20):
    print("星座為:牡羊座")
elif (month == 4 and 21<=day<=30) or (month == 5 and 1<=day<=21):
    print("星座為:金牛座")
elif (month == 5 and 22<=day<=31) or (month == 6 and 1<=day<=21):
    print("星座為:雙子座")
elif (month == 6 and 22<=day<=30) or (month == 7 and 1<=day<=22):
    print("星座為:巨蟹座")
elif (month == 7 and 23<=day<=31) or (month == 8 and 1<=day<=23):
    print("星座為:獅子座")
elif (month == 8 and 24<=day<=31) or (month == 9 and 1<=day<=23):
    print("星座為:處女座")
elif (month == 9 and 24<=day<=30) or (month == 10 and 1<=day<=23):
    print("星座為:天秤座")
elif (month == 10 and 24<=day<=31) or (month == 11 and 1<=day<=22):
    print("星座為:天蠍座")
elif (month == 11 and 23<=day<=30) or (month == 12 and 1<=day<=21):
    print("星座為:射手座")
elif (month == 12 and 22<=day<=31) or (month == 1 and 1<=day<=20):
    print("星座為:魔羯座")
else:
    print("日期超出範圍")