N = int(input())
arr_x = []
arr_y = []
arr = []
ans = [-1]*N

for _ in range(N):
    x,y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
    arr.append([x,y])
    
for x in arr_x:
    for y in arr_y:
        dis  = []
        for ex,ey in arr:
            dis.append(abs(x-ex) + abs(y-ey))
            
        dis.sort()
        tem = 0
        for i in range(len(dis)):
          tem += dis[i]
          if ans[i] == -1:
            ans[i] = tem
          else:
            ans[i] = min(ans[i], tem)
            
print(*ans)