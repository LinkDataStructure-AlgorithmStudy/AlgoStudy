N,M = map(int,input().split())

lst = []
for i in range(N):
    lst.append(list(map(int,input())))

cnt = 0

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
        #들른 곳 좌표
        lst[x][y] = 1

        #상하좌우 이동
        for i in range(4):
            lx = x + dx[i]
            ly = y + dy[i]

            #내부에 있을 때
            if(lx >= 0 and lx < N and ly >= 0 and ly < M):
                if (lst[lx][ly] == 0):
                    dfs(lx,ly)


for i in range(N):
    for j in range(M):
        if (lst[i][j] == 0):
            dfs(i,j)
            cnt += 1

print(cnt)