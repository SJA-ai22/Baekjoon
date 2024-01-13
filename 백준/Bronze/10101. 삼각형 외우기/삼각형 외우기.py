a = int(input())
b = int(input())
c = int(input())
result = ''
if a+b+c == 180:
    if a == b or b ==c or a == c:
        result = 'Isosceles'
        if a == b == c:
            result = 'Equilateral'
    else:
        result = 'Scalene'
else:
    result = 'Error'
print(result)