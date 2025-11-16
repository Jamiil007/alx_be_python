task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_text = "high priority task"
    case "medium":
        priority_text = "medium priority task"
    case "low":
        priority_text = "low priority task"
    case _:
        priority_text = "task with an unknown priority level"

if time_bound == "yes":
    final_message = f"Reminder: '{task}' is a {priority_text} that requires immediate attention today!"
else:
    final_message = f"Reminder: '{task}' is a {priority_text} and is not time-sensitive."

print(final_message)
