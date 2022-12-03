N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#리스트 정렬
A.sort()
B.sort(reverse = True)

#비교 후 바꾸기
for i in range(K):
    if(A[i] < B[i]):
        A[i] = B[i]
    
    else:
        break

print(sum(A))