# entry point, menu loop, user I/O

# ______________ Objective:
# A CLI app where users add tasks, mark them done, track recurring habits, and 
# save/load their data to a file — with a small stats report at the end

# ______________ Core functionalities
# Add tasks — give it a title and a priority (low/medium/high).
# Add recurring tasks — same as above, but tagged with a frequency (daily/weekly), so they behave a little differently from a normal one-off task.
# List tasks — see everything, or just what's pending vs. completed.
# Mark tasks done — updates the task's internal state.
# View stats — completion percentage, counts, and a couple of small computed numbers.
# Random extras — a motivational quote, or a shuffle feature to "surprise" you with what to work on next.
# Persistence — saves to a file on exit, loads from it on startup, so your list survives between sessions.

from tasks import Task, RecurringTask
from task_utils import Menu

menus = Menu()

#⬇️ Store tasks as a list of Task/RecurringTask objects.
all_tasks = []

#⬇️ Main 'main.py' program:
menus.menu_1()

try:
    user_choice = int(input("Choose one numerical option:\n"))
except ValueError:
    print("Invalid entry. Cannot leave field blank or enter non-numerical entry")


# ⬇️Add tasks — give it a title and a priority (low/medium/high).
if user_choice == 1:
    task_type = int(input("Task type — (1) One-time or (2) Recurring?:\n"))

    if task_type == 1:
        title_input = input("Enter task title:\n")
        priority_input = input("Enter one of the following choices (low/medium/high):\n").lower()
        new_task = Task(title=title_input, priority=priority_input)
    elif task_type == 2:
        title_input = input("Enter task title:\n")
        priority_input = input("Enter one of the following choices (low/medium/high):\n").lower()
        frequency = input("Enter 'D' for Daily, or 'W' for Weekly:\n")
        new_task = RecurringTask(frequency=frequency)
elif user_choice == 2:
    pass
elif user_choice == 3:
    pass
elif user_choice == 4:
    pass
elif user_choice == 5:
    pass
else:
    print(f"{user_choice} is not a option. Try again.")

