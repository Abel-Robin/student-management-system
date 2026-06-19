from students import add_student, view_students, search_student, delete_student, update_student,sort_by_marks
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Sort by Marks")
    print("7. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        add_student(sid, name, age, grade)

    elif choice == "2":
        students = view_students()
        for s in students:
            print(s)

    elif choice == "3":
        sid = input("Enter ID: ")
        result = search_student(sid)
        print(result if result else "Not found")

    elif choice == "4":
        sid = input("Enter ID: ")
        delete_student(sid)

    elif choice == "5":
        sid = input("Enter ID to update: ")
        name = input("New Name: ")
        age = input("New Age: ")
        grade = input("New Grade: ")
        update_student(sid, name, age, grade)
        print("Student updated successfully")
    elif choice == "6":
        sort_by_marks()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
