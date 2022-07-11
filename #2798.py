N, goal = map(int, input().split())
num = list((input().split()))

A = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = int(num[i]) + int(num[j]) + int(num[k]) #세 수를 더하는 모든 경우의 수..!
            if sum <= goal:
                A.append(sum) #goal 이하의 수들을 A에 따로 저장해 놓기 

print(max(A))
