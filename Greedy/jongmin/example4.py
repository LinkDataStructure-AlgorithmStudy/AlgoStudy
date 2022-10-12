N, K = map(int, input().split())
cnt = 0#연산 횟수 세기
while True:
  if N%K==0:#K의 배수라면
    N = N / K
    cnt += 1
    if N==1: break
  
  else: #K의 배수가 아니라면
    N = N - 1
    cnt += 1
    if N==1: break

print(cnt)

#이 소스코드는 N이 100억 이상의 숫자라면 매우 오래걸린다
