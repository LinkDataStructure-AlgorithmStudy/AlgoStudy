N, M = map(int, input().split())

cards = [] #숫자 카드를 저장할 리스트
max_number = []#카장 큰 숫자들 저장할 리스트

for i in range(N):
  tmp = min(list(map(int, input().split())))#입력받은 숫자 카드들 중에서 가장 작은 값
  #한 행에서 가장 작은 값
  max_number.append(tmp)
  #각 행에서 가장 작은 값들 중에서 가장 큰 값

print(max(max_number))

