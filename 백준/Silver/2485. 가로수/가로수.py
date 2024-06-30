n = int(input())

data = []
sub = []
for i in range(n):
  data.append(int(input()))
  if i >= 1:
    sub.append(data[i]-data[i-1])

def gcd(a,b):
  while b > 0:
    a, b = b, a % b
  return a

max_gcd = sub[0]
for j in range(n-1):
  max_gcd = gcd(sub[j], max_gcd)

cnt = 0
for k in range(n-1):
  cnt += sub[k]//max_gcd - 1

print(cnt)