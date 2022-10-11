N, M, K = map(int,input().split())
arr = list(map(int,input().split()))

###내림차순 정렬
arr.sort(reverse=True)

sum = 0
n = 1
m = 1

###가장 큰 수를 K번 더하기
###K번만큼 더한 후 배열의 두 번째 인덱스를 더한 후 다시 반복
for i in range(1,M+1):
    if (i == (K+1)*n):
        sum += arr[1]
        n += 1
    else:
        sum += max(arr)

print(sum)