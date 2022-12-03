n = int(input())

###입력키 리스트 받기
key = list(map(str,input().split()))

x = 1
y = 1

for i in key:
    ###사각형 크기보다 작을 때 수행
    if(x < n and y < n):
        if(i == "R"):
            x += 1
        elif(i == "L"):
            x -= 1
        elif(i == "U"):
            y -= 1
        elif(i == "D"):
            y += 1
    ###사각형 크기보다 크면 넘어가기
    else:
        continue
    ###좌표가 0일 때 처리
    if (x == 0):
        x += 1
    elif (y == 0):
        y += 1

print(y, x)