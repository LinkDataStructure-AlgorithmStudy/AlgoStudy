N, K = map(int,input().split())

cnt = 0

###N이 나누어 떨어지면 몫을 저장
###아니라면 1만큼 빼는 연산
###N이 1일때 종료
while(1):
    if (N % K == 0):
        N //= K
        cnt += 1
    else:
        N -= 1
        cnt += 1

    if(N == 1):
        break

print(cnt)
