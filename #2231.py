def f_power(num): #몇자리의 수인지 구하는 함수(6자리 이하)
    for i in range(6):
        if num / pow(10, i) < 1:
            return i

def f_separate(n): #입력한 수를 숫자를 쪼개어 리스트로 저장하는 함수
    ans = []
    while n > 0:
        temp = int(n%10)
        ans.insert(0, temp)
        n = int((n - temp) / 10) #int() 추가하니까 name-error 해결되었다.
        
    while len(ans) != 6:
        ans.insert(0, 0)   
    return ans
        

num = int(input())
p = f_power(num)
target = num - 9 * p #각 자리의 수가 9 이하 이므로, 9*p보다 작은수부터 생성자인지 조사하면 된다고 생각했다. 

while target < num:
    temp = f_separate(target)
    ans = target + temp[0] + temp[1] + temp[2] + temp[3] + temp[4] + temp[5]

    if ans == num:
        print(target)
        break
    else:
        target += 1
        if target == num:
            print(0)
