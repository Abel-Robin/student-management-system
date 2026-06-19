import csv

FILE = "database.csv"

def format_student(row):
    return {
        "id": row[0],
        "name": row[1],
        "age": int(row[2]),
        "grade": row[3]
    }


def add_student(student_id, name, age, grade):
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, int(age), grade])


def view_students():
    with open(FILE, "r") as file:
        reader = csv.reader(file)
        return [format_student(row) for row in reader]


def delete_student(student_id):
    students = view_students()
    updated_list = []

    for student in students:
        if student["id"] != student_id:
            updated_list.append([student["id"], student["name"], student["age"], student["grade"]])

    with open(FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_list)


def search_student(student_id):
    students = view_students()

    for student in students:
        if student["id"] == student_id:
            return student

    return None

def update_student(student_id, new_name, new_age, new_grade):
    students = view_students()
    updated_list = []

    for student in students:
        if student["id"] == student_id:
            student["name"] = new_name
            student["age"] = int(new_age)
            student["grade"] = new_grade

        updated_list.append([
            student["id"],
            student["name"],
            student["age"],
            student["grade"]
        ])

    with open(FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_list)

def sort_by_marks():
    students = view_students()

    if not students:
        print("No data found.")
        return

    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter choice: ")

    if choice == "1":
        students.sort(key=lambda x: int(x["grade"]))
    elif choice == "2":
        students.sort(key=lambda x: int(x["grade"]), reverse=True)
    else:
        print("Invalid choice")
        return

    for s in students:
        print(s["id"], s["name"], s["age"], s["grade"])
