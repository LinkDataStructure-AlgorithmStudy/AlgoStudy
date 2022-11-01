N = int(input())#금액을 입력

coin = [500,100,50,10] #coin의 종류
sum = 0

for i in coin:
  sum = sum + N // i #해당 동전이 몇 개가 들어가는지

  print("{}원 : {}개".format(i, N//i))

  N = N % i #해당 동전을 다 쓰고 난 나머지 금액

print("총",sum,"개")
