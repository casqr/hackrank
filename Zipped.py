"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
 """

N, X = list(map(float, (input().split())))
sub_grades = []
for _ in range(int(X)):
    stud_grade = list(map(float, (input().split())))[:int(N)]
    sub_grades.append(stud_grade)

for grades in zip(*sub_grades):
    print(round(sum(grades) / len(grades), 1))
