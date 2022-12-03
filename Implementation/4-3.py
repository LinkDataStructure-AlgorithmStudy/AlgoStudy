###체스판 좌표
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = [1, 2, 3, 4 ,5, 6, 7, 8]

data = list(input())

###위치를 좌표화
loc = [row.index(data[0]), col.index(int(data[1]))]

###나이트가 이동하는 경우의 수
mov = [[-2,-1], [-2,1], [2,1], [2,-1], [1,-2], [1,2], [-1,2], [-1,-2]]

###더한 후 0보다 크면 카운트
cnt = 0
for x,y in mov:
    x += loc[0]
    y += loc[1]
    
    if (x > 0 and y > 0):
        cnt += 1
    
print(cnt)