N, M = map(int,input().split())

result = []

for j in range(N):
    lst = list(map(int,input().split()))
    result.append(min(lst))

print(max(result))
