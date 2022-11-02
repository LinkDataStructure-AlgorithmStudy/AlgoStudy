
n=int(input())
clock=[0 for i in range(6)]
cnt=0

for i in range(n+1):
    if clock[1]<9:
        clock[1]=i
    else:
        clock[0]=i//10
        clock[1]=0
    clock[3],clock[2]=0,0

    for j in range(60):
        if clock[3]<9:
            clock[3]+=1
        else:
            clock[2]+=1
            clock[3]=0
        clock[4],clock[5]=0,0

        for k in range(60):
            if clock[5]<9:
                clock[5]+=1
            else:
                clock[4]+=1
                clock[5]=0
            print(clock)
            for l in range(0,6):
                if clock[l]==3:
                    cnt+=1
                    break
               
print(cnt)
        