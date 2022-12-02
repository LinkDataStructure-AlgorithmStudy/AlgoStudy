#큰 수의 법칙-M,K//M번 더하기, K번 연속으로 더해질 수 없음-좀 더 깔끔한 코드
#입력
N,M,K=map(int,input().split())
lst=list(map(int,input().split()))

lst.sort(reverse=True) #내림차순 정렬
tmp=M//(K+1) #총 몇 번 반복될지 계산
remain=M%(K+1) #위 계산 후 나머지 횟수 구하기
sum=lst[0]*(K*tmp+remain)+lst[1]*tmp

print(sum)