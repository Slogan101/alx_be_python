task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time = input("Is it time-bound? (yes/no):")

if priority == "high":
    print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
elif priority == "high" and time == "no":
    print(f"Reminder: {task} is a {priority} priority task that requires your attention!")
elif priority == "medium" and time == "yes":
    print(f"Note: {task} is a {priority} priority task. Consider completing it before the set time.")
elif priority == "medium" and time == "no":
    print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
elif priority == "low" and time == "yes":
    print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
elif priority == "low" and time == "no":
    print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")