score = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
total = 0
result = 0

for _ in range(20) :
    title, my_grade, my_score = input().split()
    my_grade = float(my_grade)
    if my_score != 'P' :
        total += my_grade
        result += my_grade * grade[score.index(my_score)]

print(result / total)