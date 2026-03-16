tasks = []

while True:
    print("\n---TO DO LIST---")
    print("1. Add Task")
    print("2.View Task")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if tasks == []:
            print("No tasks available")
        else:
            print("Your tasks are: ")
            i = 1
            for x in tasks:
                print(i,x)
                i = i + 1

    elif choice == 3:
        num = int(input("Enter task number to update: "))
        if num >= 1 and num <= len(tasks):
            new = input("Enter new task: ")
            tasks[num-1] = new
            print("Task updated")
        else:
            print("Invalid number")

    elif choice == 4:
        num = int(input("Enter task number to delete: "))
        if num <=len(tasks):
            tasks.pop(num-1)
            print("Task deleted")
        else:
            print("Invalid number")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Your choice is invalid.Please Try again!")



