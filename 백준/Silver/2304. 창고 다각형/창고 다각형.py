n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort()
max_b = 0
num = 0
cnt = 0
for i in arr:
  if max_b < i[1]:
    max_b = i[1]
    num = cnt
  cnt += 1

result = max_b
left_b = arr[0][1]
left_a = arr[0][0]
for i in range(num):
  if left_b <= arr[i+1][1]:
    result += left_b * (arr[i+1][0]-left_a)
    left_b = arr[i+1][1]
    left_a = arr[i+1][0]

right_b = arr[-1][1]
right_a = arr[-1][0]
for i in range(n-num-1):
  if right_b <= arr[n-i-2][1]:
    result += right_b * ((right_a+1)-(arr[n-i-2][0]+1))
    right_b = arr[n-i-2][1]
    right_a = arr[n-i-2][0]

print(result)