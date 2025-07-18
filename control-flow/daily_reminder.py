while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: {task} is a high priority task. Try to complete it as soon as possible.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
            else:
                print(f"Note: {task} is a medium priority task. You can complete it when you have time.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: {task} is a low priority task that requires immediate attention today!")
            else:
                print(f"Note: {task} is a low priority task. You can complete it whenever you have time.")
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            continue  # Restart loop if input is invalid

    again = input("Do you want to enter another task? (yes/no): ")
    if again != "yes":
        print("Goodbye. Stay productive!")
        break