def get_grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 65:
        return 'D'
    else:
        return 'F'

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville":62
}

student_grades = {}

for key,val in student_scores.items():
    student_grades[key] = get_grade(val)

print(student_grades)