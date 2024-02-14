import sys
n, m = map(int, input().split())
name = {}
index = {}

for i in range(1, n+1):
    a = sys.stdin.readline().strip()
    index[i] = a
    name[a] = i

for j in range(m):
    b = sys.stdin.readline().strip()
    if b.isnumeric():
        print(index[int(b)])
    else:
        print(name[b])