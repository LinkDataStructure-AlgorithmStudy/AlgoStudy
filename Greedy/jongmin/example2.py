N, M, K = map(int,input().split())

numbers = list(map(int,input().split()))

first = max(numbers)
numbers.pop(numbers.index(first))
second = max(numbers)

sum = 0
while True:
  if M:
    if M>K:
      for i in range(K):
        sum += first
        M -= 1


      if not M:
        break
      if M:
        sum += second
        M-=1
        if not M:
          break

    else:
      for i in range(M):
        sum+=first
        M -= 1
      
      
      if not M:
          break
      if M:
        sum += second
        M-=1
        if not M:
          break
        
  if not M:
    break

print(sum)
