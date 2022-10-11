n = int(input())
count = 0

coin = [500, 100, 50, 10]

###입력받은 돈을 동전 별로 나눈 몫를 더하며 저장
###나머지 돈으로 반복
for i in coin:
    count += n//i
    n %= coin

print(count)