from datetime import datetime

file_name = "study_log.txt"

while True:
    print("\n1. Create new study log")
    print("2. Add a new study entry")
    print("3. View all study entries")
    print("4. Erase all study entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        file_name = input("Enter the new file name: ")
        open(file_name, 'w').close()
        print(f"New study log '{file_name}' created.")

    elif choice == '2':
        date = input("Enter the date of your study: ")
        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        topic = input("Enter the topic of your study: ")
        if topic == "":
            topic = "No Topic"

        time_amount = input("Enter the amount of time you studied: ")
        entry = input("Study entry: ")

        with open(file_name, 'a') as file:
            file.write(f"Date: {date}\n")
            file.write(f"Topic: {topic}\n")
            file.write(f"Time spent: {time_amount}\n")
            file.write(f"{entry}\n")
            file.write("-" * 30 + "\n")

        print("Entry added.")

    elif choice == '3':
        try:
            with open(file_name, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("No study entries yet.")

    elif choice == '4':
        open(file_name, 'w').close()
        print("All entries erased.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
