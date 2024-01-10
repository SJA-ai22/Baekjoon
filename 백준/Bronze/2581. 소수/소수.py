min = int(input())
max = int(input())
plus ,min_num = 0, 0
count = 0
for i in range(min, max+1):
    if i == 2:
        min_num = 2
        count = 1
        plus = 2
    else:
        b = int(i/2)+1
        for j in range(2,b+1):
            if i % j == 0:
                break
            elif j == b:
                plus += i
                if count == 0:
                    count = 1
                    min_num = i
if count == 0:
    print(-1)
else:
    print(plus)
    print(min_num)