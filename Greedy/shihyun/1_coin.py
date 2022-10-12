#3-1거스름돈
n=int(input())
coin=[500,100,50,10]

result=[0,0,0,0]
for i in range(4):
    result[i]=n//coin[i]
    n-=result[i]*coin[i]

print(sum(result))