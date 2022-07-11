word = list(input())
n = len(word)
m = n

dic1 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
dic2 = ['dz=']
        
for i in range(len(word)-1):
    if word[i]+word[i+1] in dic1:
        m -= 1
            
for i in range(len(word)-2): #위에서 구한 'z='가 사실은 'dz='일수도 있으므로 체크한다.
    if word[i]+word[i+1]+word[i+2] in dic2:
        m -= 1

print(m)
