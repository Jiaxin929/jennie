a=int(input("請輸入比數:"))
dict1 = {}
for i in range(a):
    b,c = input("輸入單字:").split()
    dict1[b] = c

j = str(input("輸入查詢單字"))

print(f'{j}中文意思為{dict1[j]}')