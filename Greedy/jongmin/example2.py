N, M, K = map(int,input().split())#N,M,K는 순서대로 배열 길이, 총 덧셈 횟수, 연속 가능한 덧셈 횟수

numbers = list(map(int,input().split())) #숫자 리스트 입력

first = max(numbers)#입력 받은 숫자들 중에서 가장 큰 값(제일 큰 수)
numbers.pop(numbers.index(first))#가장 큰 값을 리스트에서 제외
second = max(numbers)#남은 리스트 숫자들 중에서 가장 큰 값(두 번째로 큰 수)

sum = 0 #만들 수 있는 가장 큰 수
while True: #하나하나 시뮬레이션 돌리기
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
