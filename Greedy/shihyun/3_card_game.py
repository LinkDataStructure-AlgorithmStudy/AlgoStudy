#숫자 카드게임
#M*N행렬-선택된 행에서 가장 작은 값-최종적으로는 가장 큰 값 찾기
import sys
M,N=map(int,input().split())
lst=[] #2차원 배열 초기화
max=0
#2차원 배열 입력
for i in range(N):
    lst=list(input().split())
    lst.sort() #작은거부터 정렬
    print(lst)    
    if max<lst[0]:
        max=lst[0]

print(max)