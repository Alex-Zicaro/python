
def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 40:
            rounded_grades.append(grade)
        elif grade % 5 >= 3:
            rounded_grades.append(grade + (5 - grade % 5))
        else:
            rounded_grades.append(grade)
    return rounded_grades