# Initialising Dictionary
student_grades = {  }

# Adding Student
def add_student(name,grade):
    if name in student_grades:
        print("Student already exists!")

    else:
        student_grades[name] = grade

# Update Student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with grade {grade} is updated ")
    else:
        print(f"{name} is not found!")

# Delete Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"{name} is not found!")

# View Students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

    else:
        print("No Student Found/Added!")

def main():
    while True:
        print("\nStudent Grades Management System\n")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("\nEnter your choice:"))
        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            update_student(name,grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Exiting the Program!")
            break

        else:
            print("Invalid Inputs!")

main()