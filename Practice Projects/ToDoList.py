def task():
    tasks = []
    print("Welcome To The Task Manager\n")

    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"\nToday's tasks are: \n{tasks}\n")

    while True:
        operation = int(input("Enter 1: Add new task\nEnter 2: Update task\nEnter 3: Delete task\nEnter 4: View tasks\nEnter 5: Exit/Stop\nEnter: "))
        if operation == 1:
            add = input("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been successfully added !\n")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task updated successfully !\n")
            else:
                print("Task not found!")

        elif operation == 3:
            del_val = input("Which task you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted..")
            else:
                print("Task not found!")

        elif operation == 4:
            print(f"Total Tasks: {tasks}")

        elif operation == 5:
            print("\nClosing the program..")
            break

        else:
            print("Invalid Inputs..\n")

task()

