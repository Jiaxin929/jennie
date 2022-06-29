a = int(input("請輸入一個正整數(<10):"))

total = 1

for i in range(1, a+1):
    for c in range(1, i+1):
        print(total, end =" ")
        total+=1
    print()