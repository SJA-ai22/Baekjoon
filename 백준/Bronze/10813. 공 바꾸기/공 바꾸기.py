num, n = map(int, input().split())
bascket = list(range(1,num+1,1))
for i in range(n):
  a,b =map(int, input().split())
  c = bascket[a-1]
  bascket[a-1] = bascket[b-1]
  bascket[b-1] = c
print(*bascket)