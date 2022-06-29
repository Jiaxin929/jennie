team = int(input("組數為:"))
for i in range(1,team+1):
    a = list(input("輸入全票、半票張數(例3 4):"))
    print("第",i,"組應收的費用為:",int(a[0])*250+int(a[2])*175)