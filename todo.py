

print('1. Add tasks. ' \
'\n2. View all tasks. ' \
'\n3. Mark tasks as done. ' \
'\n4. Delete tasks. ' \
'\n5. Exit')

choice = input('Choose an option: ')

while True:

    if choice == '1':
        task = input(f'Enter the task description: ')
        with open('tasks.txt', 'a') as file:
            file.write(f"[ ] {task}\n")
        print('Task added.')
    
    elif choice == '2':
        try:
            with open('tasks.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print('No tasks found.')
    
    elif choice == '3':
        try:
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks to mark as done.")
                continue

            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")

            task_num = input("Enter the task number to mark as done: ")
            if not task_num.isdigit() or int(task_num) < 1 or int(task_num) > len(tasks):
                print("Invalid task number.")
                continue

            index = int(task_num) - 1

            if tasks[index].startswith("[X]"):
                print("Task is already done!")
            else:
                tasks[index] = tasks[index].replace("[ ]", "[X]", 1)
                print(f"Task #{task_num} marked as done.")

            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)

        except FileNotFoundError:
            print("No tasks found.")

    
    elif choice == '4':
        open('tasks.txt', 'w').close()
        print('All tasks deleted.')

    elif choice == '5':
        print('Exiting...')
        break
    else:
        print('Invalid choice, try again.')
        continue