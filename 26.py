while(True):
    a=input("檢測的字串(end結束):")
    if(a=="end"):
       print("檢測結束")
       break     
    else:
       b=str(input("請輸入要檢測的單一字元:"))
       n= a.count(b)
       print("字元",b,"出現次數為:",n)
       break