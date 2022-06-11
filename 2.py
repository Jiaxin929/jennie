e = int(input("請輸入一個度數（正整數）"))
a=0
b=0
if e <= 120:
    a = e*2.10
    b = e*2.10
elif 121 <= e <=330:
    a = e*3.02
    b = e*2.68
elif 331 <= e <=500:
    a = e*4.39
    b = e*3.61
elif 501 <= e <=700:
    a = e*4.97
    b = e*4.01
else:
    a = e*5.63
    b = e*4.50

print("Summer months:%.2f" %(a))
print("Non-Summer months:%.2f" %(b))