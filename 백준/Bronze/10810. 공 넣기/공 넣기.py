num, n = map(int, input().split())
bascket = [0] * num
for i in range(n):
  a,b,c =map(int, input().split())
  while(a-1 < b):
    bascket[a-1] = c
    a += 1
print(*bascket)