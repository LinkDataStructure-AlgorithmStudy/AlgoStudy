N, M = map(int,input().split())

result = []

###N번만큼 리스트 입력
###리스트중 최소값을 저장
###최소값이 저장된 리스트에서 max를 사용
for j in range(N):
    lst = list(map(int,input().split()))
    result.append(min(lst))

print(max(result))
