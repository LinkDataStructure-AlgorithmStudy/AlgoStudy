#시간복잡도 O(n),2n이지만,,

n=int(input())
gps=[1,1]
lst=list(input()) #이동 위치 입력
num=len(lst)

for i in range(num):
    if lst[i]=="R":
        if gps[1]<5:
            gps[1]+=1

    elif lst[i]=="L":
        if gps[1]>1:
            gps[1]-=1

    elif lst[i]=="U":
        if gps[0]>1:
            gps[0]-=1

    elif lst[i]=="D":
        if gps[0]<5:
            gps[0]+=1

print(gps[0],gps[1])