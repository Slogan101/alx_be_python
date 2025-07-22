task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time = input("Is it time-bound? (yes/no):")

if priority == "high":
    if time == "yes":
        print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
elif priority == "high":
    if time == "no":
        print(f"Reminder: {task} is a {priority} priority task that requires your attention!")
elif priority == "medium":
    if time == "yes":
        print(f"Note: {task} is a {priority} priority task. Consider completing it before the set time.")
elif priority == "medium":
    if time == "no":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
elif priority == "low":
    if time == "yes":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
elif priority == "low":
    if time == "no":
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")