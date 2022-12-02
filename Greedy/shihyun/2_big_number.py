#큰 수의 법칙-M,K 각각 특정한인덱스의 수가 연속해서 K번만 더해질 수있다M번 더하기
#입력
N,M,K=map(int,input().split())
lst=list(map(int,input().split()))

sum=0
lst.sort(reverse=True)
print(lst)
i=0
while(True):
    if i!=0:
        sum+=lst[i] #가장 큰 수가 아닐 때는 한번만 더하고 넘어가기
        i=0
        M-=1
    else:
        if M<K:
            sum+=lst[i]*M
        else:
            sum+=lst[i]*K #큰 수일 수록 많이 더해줘야함
        i=1
        M-=K #횟수 차감
    print(sum)
    if M<=0:  #다 더해줬으면 break
        break
print(sum) #합 출력
    