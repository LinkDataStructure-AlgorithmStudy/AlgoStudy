N = int(input())

spot = [1,1]
command = list(map(str, input().split()))

for i in command:
  if i == "R": spot[1] += 1

  elif i == "L": spot[1] -= 1

  elif i == "U" : spot[0] -= 1

  elif i == "D" : spot[0] += 1

  if spot[0] == 0 : spot[0] += 1

  elif spot[0] == N+1 : spot[0] -= 1
  
  elif spot[1] == 0 : spot[1] += 1

  elif spot[1] == N+1 : spot[1] -= 1

print(spot[0], spot[1])

