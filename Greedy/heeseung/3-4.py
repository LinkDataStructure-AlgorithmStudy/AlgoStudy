N, K = map(int,input().split())

cnt = 0

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
