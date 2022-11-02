h = int(input())

cnt = 0

###h시간, 60분, 60초 동안 반복
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            ###개수를 세기 위한 연산
            if((i//10 == 3 or i%10 == 3)):
                cnt += 1
            elif((j//10 == 3 or j%10 == 3)):
                cnt += 1
            elif((k//10 == 3 or k%10 == 3)):
                cnt += 1
                
print(cnt)