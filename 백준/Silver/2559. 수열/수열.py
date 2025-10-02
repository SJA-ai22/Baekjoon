N, K = map(int,input().split())
arr = list(map(int,input().split()))
max = -10**7
st = 0
cnt = 0
for i in range(N-K+1):
    if i == 0:
        for j in range(K):
            cnt += arr[j]
        max = cnt
    else:
        cnt += arr[K+st]-arr[i-1]
        st += 1
        if max < cnt:
            max = cnt
print(max)