from students import add_student, view_students, delete_student, search_student
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            add_student(sid, name, age, grade)
            print("Student added!")

        elif choice == "2":
            students = view_students()
            for s in students:
                print(s)

        elif choice == "3":
            sid = input("Enter ID: ")
            student = search_student(sid)
            print(student if student else "Not found")

        elif choice == "4":
            sid = input("Enter ID to delete: ")
            delete_student(sid)
            print("Deleted if existed.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
