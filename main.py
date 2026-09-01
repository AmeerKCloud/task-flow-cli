# entry point, menu loop, user I/O

# ______________ Objective:
# A CLI app where users add tasks, mark them done, track recurring habits, and 
# save/load their data to a file — with a small stats report at the end

# ______________ Core functionalities
# Add tasks — give it a title and a priority (low/medium/high). ✅
# Add recurring tasks — same as above, but tagged with a frequency (daily/weekly), so they behave a little differently from a normal one-off task. ⚠️
# List tasks — see everything, or just what's pending vs. completed.
# Mark tasks done — updates the task's internal state.
# View stats — completion percentage, counts, and a couple of small computed numbers.
# Random extras — a motivational quote, or a shuffle feature to "surprise" you with what to work on next.
# Persistence — saves to a file on exit, loads from it on startup, so your list survives between sessions.

# TODO:
# Currently working on Part 3 — Data & Logic: 11, 12, 13, & 14 (see 'taskflow_project_spec' doc in google drive).


from tasks import Task, RecurringTask
from task_utils import Menu, VALID_PRIORITIES, PRIORITY_WEIGHTS

menus = Menu()

MAX_TASKS = 20

#⬇️ Store tasks as a list of Task/RecurringTask objects.
all_tasks = []

total_completed = 0

#⬇️ Main 'main.py' program from here onwards:

while True:

    menus.menu_1()

    try:
        user_choice = int(input("Choose one numerical option:\n"))
    except ValueError:
        print("Invalid entry. Cannot leave field blank or enter non-numerical entry")
        continue   #⬅️ skip everything below, go re-print the menu and ask again


    # ⬇️Add tasks — give it a title and a priority (low/medium/high).
    if user_choice == 1:

        if len(all_tasks) < 20:

            title_input = input("Enter task title:\n")
            priority_input = input("Enter one of the following choices (low/medium/high priority):\n").lower()
            task_type = int(input("Task type — (1) One-time or (2) Recurring?:\n"))

            if task_type == 1:
                if priority_input == "":
                    one_time = Task(title=title_input)
                elif priority_input in VALID_PRIORITIES:
                    one_time = Task(title=title_input, priority=priority_input)
                else:
                    print("That is not a valid option.")
                all_tasks.append(one_time)
            elif task_type == 2:
                frequency = input("Enter 'D' for Daily, or 'W' for Weekly:\n")
                habit = RecurringTask(title=title_input, priority=priority_input, frequency=frequency)
                all_tasks.append(habit)
        else:
            print(f"You have reached your limit of {MAX_TASKS}. Complete some tasks before adding more.")
    elif user_choice == 2:
        for task in all_tasks:
            print(task.describe())
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass
    elif user_choice == 5:
        break
    else:
        print(f"{user_choice} is not a option. Try again.")

# Saved to github..