import csv

FILE = "database.csv"


def add_student(student_id, name, age, grade):
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, grade])


def view_students():
    with open(FILE, "r") as file:
        reader = csv.reader(file)
        return list(reader)


def delete_student(student_id):
    students = view_students()
    updated_list = []

    for student in students:
        if student[0] != student_id:
            updated_list.append(student)

    with open(FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_list)


def search_student(student_id):
    students = view_students()

    for student in students:
        if student[0] == student_id:
            return student

    return None
