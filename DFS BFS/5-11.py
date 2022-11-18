from collections import deque

N,M = map(int,input().split())

lst = []
for i in range(N):
    lst.append(list(map(int,input())))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때까지
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            lx = x + dx[i]
            ly = y + dy[i]

            #내부 제한
            if(lx < 0 or ly < 0 or lx >= N or ly >= M):
                continue
            if(lst[lx][ly] == 0):
                continue
            #첫 방문시 기록
            if(lst[lx][ly] == 1):
                lst[lx][ly] = lst[x][y] + 1
                queue.append((lx,ly))
    return lst[N-1][M-1]

print(bfs(0,0))