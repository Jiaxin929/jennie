y = []

for i in range(2):
    a = input("請輸入日、月:")
    y.append(a)

m = int(y[0])
d = int(y[1])

s = int((m*2|d)%3)
if s == 0:
    print("普通")
elif s == 1:
    print("吉")
elif s == 2:
    print("大吉")