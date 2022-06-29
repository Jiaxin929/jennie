ranG = range(1,11)
a = []
for i in ranG:
    
    print("請輸入第",i,"個數字:")
    c = int(input())
    a.append(c)

a.sort() #小到大排序
a.reverse() 
print("最大的數字",a[0],a[1],a[2])
a.reverse()
print("最小的數字",a[0],a[1],a[2])