n, m = map(int, input().split())
Ndata = []
count = 0

for i in range(n):
    Ndata.append(input())
    
for j in range(m):
    check = input()
    if check in Ndata:
        count += 1
print(count)