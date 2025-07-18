
Task = input("Enter your Task: ")
Priority = input("Enter Task Priority (high/medium/low): ")
Time_Bound = input("Is this a time bount Task? (yes/no): ")
match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: {Task} is a high Priority Task that requires immeadiate attention today!")
        else:
            print(f"Note: {Task} is a high Priority Task. Try to complete it as soon as possible.")
    case "medium":
        if Time_Bound == "yes":
            print(f"Reminder: {Task} is a medium Priority Task that should be completed soon.")
        else:
            print(f"Note: {Task} is a medium Priority Task. You can complete it when you have time.")
    case "low":
        if Time_Bound == "yes":
            print(f"Reminder: {Task} is a low Priority Task that can be completed at your convenience.")
        else:
            print(f"Note: {Task} is a low Priority Task. You can complete it whenever you have time.")
    case _:
        print("Invalid Priority. Please enter high, medium, or low.")