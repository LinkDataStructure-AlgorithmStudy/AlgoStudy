N, M = map(int,input().split())
x, y, d = map(int,input().split())

###맵 입력
maps = []
for i in range(N):
    maps.append(list(map(int,input().split())))

###방향에 따른 이동
dx = [-1,0,1,0]
dy = [0,1,0,-1]

###처음 위치 표시
maps[x][y] = 1
cnt = 1
dir = 0

while (1):
    ###서쪽 바라보기 // 반복
    d -= 1
    if (d < 0):
        d = 3
    
    ###이동 후 위치
    lx = x + dx[d]
    ly = y + dy[d]
    
    ###가보지 않은 곳
    if (maps[lx][ly] == 0):
        maps[lx][ly] = 1
        
        x = lx
        y = ly
        
        cnt += 1
        dir = 0
        
        continue
    else:
        dir += 1
    
    ###4방향 모두 가본 칸 or 바다
    if(dir == 4):
        lx = x - dx[d]
        ly = y - dy[d]
        
        if(maps[lx][ly] == 0):
            x = lx
            y = ly
            
        else:
            break
      

print(cnt)