N=int(input())
lst=[]
for i in range(n):
    lst[i]=int(input())

lst=sorted(lst,reversed=True)

for i in lst:
    print(i,end=" ")
