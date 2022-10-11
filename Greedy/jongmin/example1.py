N = int(input())

coin = [500,100,50,10]
sum = 0

for i in coin:
  sum = sum + N // i

  print("{}원 : {}개".format(i, N//i))

  N = N % i

print("총",sum,"개")
