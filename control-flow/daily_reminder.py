
task = input("Enter your task: ")
priority = input("Enter task priority (high/medium/low): ")
time_bound = input("Is this a time bount task? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immeadiate attention today!")
        else:
            print(f"Note: {task} is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that should be completed soon.")
        else:
            print(f"Note: {task} is a medium priority task. You can complete it when you have time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that can be completed at your convenience.")
        else:
            print(f"Note: {task} is a low priority task. You can complete it whenever you have time.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")