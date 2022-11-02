
n,m=map(int,input().split())

a,b,d=map(int,input().split()) #좌표와 방향
character_gps=[a,b]
map_structure=[0 for i in range(n)]

for i in range(n):
    map_structure[i]=list(map(int,input().split()))
print(map_structure)

#입력 끝 탐색 시작

cnt=1
stuck=0 #네 방향 다 탐색했는지 찾는 변수
while(1):
    if d==0: #방향이 위쪽일 때
        if character_gps[0]>0 and map_structure[character_gps[0]-1][character_gps[1]]==0:
            character_gps[0]-=1
            map_structure[character_gps[0]][character_gps[1]]=1 #이미 가본곳은 못가게 하는 장치
            cnt+=1
            stuck=0
        else:
            d+=1
            stuck+=1
        
    
    elif d==2: #방향이 아래일 때
        if character_gps[0]<n-1 and map_structure[character_gps[0]+1][character_gps[1]]==0:
            character_gps[0]+=1
            map_structure[character_gps[0]][character_gps[1]]=1
            cnt+=1
            stuck=0
        else:
            d+=1
            stuck+=1
    elif d==1: #방향이 오른쪽일 때
        if character_gps[1]<n-1 and map_structure[character_gps[0]][character_gps[1]+1]==0:
            character_gps[1]+=1
            map_structure[character_gps[0]][character_gps[1]]=1
            cnt+=1
            stuck=0
        else:
            d+=1
            stuck+=1
    elif d==3: #방향이 왼쪽일 때
        if character_gps[1]>0 and map_structure[character_gps[0]][character_gps[1]-1]==0:
            character_gps[0]-=1
            map_structure[character_gps[0]][character_gps[1]]=1
            cnt+=1
            stuck=0
        else:
            d=0
            stuck+=1

    if stuck==4:
        break

print(cnt)