N, K = map(int, input().split())
result = N
for i in range(1,N):
  result = result*i
for j in range(1,K+1):
  result = result // j
for z in range(1,N-K+1):
  result = result // z
print(result)