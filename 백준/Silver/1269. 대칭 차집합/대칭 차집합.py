import sys
input = sys.stdin.readline

a,b = map(int, input().split())
Adata = set(map(int, input().split()))
Bdata = set(map(int, input().split()))
Acnt = a
Bcnt = b

for i in Adata:
    if i in Bdata:
        Acnt -= 1
for j in Bdata:
    if j in Adata:
        Bcnt -= 1
print(Acnt+Bcnt)