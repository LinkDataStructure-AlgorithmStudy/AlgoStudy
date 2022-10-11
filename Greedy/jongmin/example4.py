N, K = map(int, input().split())
cnt = 0
while True:
  if N%K==0:
    N = N / K
    cnt += 1
    if N==1: break
  
  else:
    N = N - 1
    cnt += 1
    if N==1: break

print(cnt)

#이 소스코드는 N이 100억 이상의 숫자라면 매우 오래걸린다
