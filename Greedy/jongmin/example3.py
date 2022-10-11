N, M = map(int, input().split())

cards = []
max_number = []

for i in range(N):
  tmp = min(list(map(int, input().split())))
  max_number.append(tmp)

print(max(max_number))

