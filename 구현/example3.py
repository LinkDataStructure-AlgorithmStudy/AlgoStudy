N = input()
cnt = 0
# 1 -> 오른쪽  -1 -> 왼쪽
# 2 -> 아래    -2 -> 위
path = [[1,1,2],[1,1,-2],[2,2,1],[2,2,-1],[-1,-1,2],[-1,-1,-2],[-2,-2,1],[-2,-2,-1]]

for i in path:
  x = ord(str(N)[0])
  y = int(str(N)[1])
  for j in i:
    if j == 1: x += 1

    elif j == 2: y += 1

    elif j == -1: x -= 1

    elif j == -2: y -= 1

  
  if (x>96 and x<105) and (y>0 and y<9):
    cnt += 1

print(cnt)


