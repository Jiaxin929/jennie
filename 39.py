c = int(input("請輸入:"))

e = c//2
g=(c-2)//2

for i in range(e+1,-1,-1):
  print(' '*i,'*'*(c-2*i),' '*i)

for i in reversed(range(g+1,0,-1)): 
  print(' '*i,'*'*(c-2*i),' '*i)