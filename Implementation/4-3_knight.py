
gps=list(input())
print(gps)
cnt=0

diff_x=abs(ord(gps[0])-ord('h'))
diff_y=abs(int(gps[1])-8)

if diff_x==0 or diff_x==7:
    if diff_y==0 or diff_y==7:
        cnt=2
    elif diff_y==1 or diff_y==6:
        cnt=3
    else:
        cnt=4
elif diff_x==1 or diff_x==6:
    if diff_y==0 or diff_y==7:
        cnt=3
    elif diff_y==1 or diff_y==6:
        cnt=4
    else:
        cnt=6
else:
    if diff_y==0 or diff_y==7:
        cnt=4
    elif diff_y==1 or diff_y==6:
        cnt=6
    else:
        cnt=8

print(cnt)