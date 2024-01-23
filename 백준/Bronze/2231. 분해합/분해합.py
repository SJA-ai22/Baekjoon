num = int(input())
for  i in range(1,num+1):
    n = sum((map(int, str(i))))
    result = n + i
    if result == num:
        print(i)
        break
    if i == num:
        print(0)