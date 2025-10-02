def gcd(a,b):
    while a % b != 0:
        tmp = a%b
        a = b
        b =tmp
    return b

N = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0

for i in range(N-1):
    for j in range(arr[i],arr[i+1]+1):
        if gcd(arr[i],arr[i+1]) == 1:
            break
        if gcd(arr[i],j) == 1:
            if gcd(arr[i+1],j) == 1:
                cnt+=1
                break
        if j == arr[i+1]:
            cnt+=2    
print(cnt)