dict2={"123 456":9000,"456 789":5000,"789 888":6000,"336 558":10000,"775 666":12000,"566 221":7000}
a = int(input("輸入查詢組數N為:"))
for i in (1,a+1):
    s = input("輸入帳密:")
    if s in dict2:
        print(dict2[s])
    else:
        print("error")
    

