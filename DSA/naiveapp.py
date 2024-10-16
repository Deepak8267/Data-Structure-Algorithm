test = 'ababbaaababa'
patt = 'aba'
n = len(test)
m = len(patt)

for i in range(n-m+1):
    j=0
    while j<m and test[i+j] == patt[j]:
        j +=1
    
    
    if j == m:
        print("String matching with index ",{i})