def get_gcd(a,b):
    while a % b != 0:
        tmp = a%b
        a = b
        b =tmp
    return b

gcd, lcm = map(int, input().split())
# A = a*gcd, B = b*gcd_ a,b는 서로소
# a*gcd * b*gcd // gcd = lcm_ a*b = lcm//gcd
hint = lcm//gcd
arr = []
for i in range(1,int(hint**0.5)+1):
    if hint % i == 0:
        if get_gcd(i,(hint//i)) == 1:
            x = arr.append([gcd*i,gcd*(hint//i),gcd*(i+(hint//i))])
     
min_sum = float('inf')
a,b = 0,0
for j in range(len(arr)):
    if arr[j][2] < min_sum:
        min_sum = arr[j][2]
        a,b = arr[j][0],arr[j][1]
print(a,b)