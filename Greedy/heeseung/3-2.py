N, M, K = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)

sum = 0
n = 1
m = 1

for i in range(1,M+1):
    if (i == (K+1)*n):
        sum += arr[1]
        n += 1
    else:
        sum += max(arr)

print(sum)