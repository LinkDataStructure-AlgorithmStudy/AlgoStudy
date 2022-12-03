N = int(input())


#리스트 입력
lst = []

for i in range(N):
    data = input().split()
    lst.append([data[0],int(data[1])])
print(lst)

lst.sort(key = lambda x : x[1])

for i in lst:
    print(i[0],end=' ')

