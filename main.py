# entry point, menu loop, user I/O

# ______________ Objective:
# A CLI app where users add tasks, mark them done, track recurring habits, and 
# save/load their data to a file — with a small stats report at the end

# ______________ Core functionalities
# Add tasks — give it a title and a priority (low/medium/high). ✅
# Add recurring tasks — same as above, but tagged with a frequency (daily/weekly), so they behave a little differently from a normal one-off task. ✅
# List tasks — see everything, or just what's pending vs. completed. ✅
# Mark tasks done — updates the task's internal state. ✅
# View stats — completion percentage, counts, and a couple of small computed numbers. ✅
# Random extras — a motivational quote, or a shuffle feature to "surprise" you with what to work on next.
# Persistence — saves to a file on exit, loads from it on startup, so your list survives between sessions.

# TODO:
# Currently working on Part 3 — Data & Logic: 11, 12, 13, & 14 (see 'taskflow_project_spec' doc in google drive).


from tasks import Task, RecurringTask
from task_utils import Menu, VALID_PRIORITIES, PRIORITY_WEIGHTS, filter_tasks, sort_tasks, validate_input, validate_priority

menus = Menu()

MAX_TASKS = 20      #⬅️ Blocks "Add task" once the 'all_tasks' list is full

#⬇️ Store tasks as a list of Task/RecurringTask objects.
all_tasks = []

total_completed = 0

#⬇️ Main 'main.py' program from here onwards:

def print_summary(all_tasks):
    """Recieves the 'all_tasks' list; calculates & prints the # & % 
    of tasks completed from the current list of task objects."""
    num_tasks_completed = 0
    total_tasks = len(all_tasks)
    for task in all_tasks:
        if task.done == True:
            num_tasks_completed += 1

    percent_completed = round((num_tasks_completed / total_tasks) * 100)

    print(f"""Total number of tasks: {total_tasks}
    Tasks completed: {num_tasks_completed}
    Tasks remaining: {total_tasks - num_tasks_completed}
    % completed: {percent_completed}""")

def mark_done():
    """
    Increments 'total_completed' every time a task is marked done.
    Accumulates & tracks total # of tasks completed over the life 
    of this program.
    """
    global total_completed
    total_completed += 1
    return total_completed


while True:

    menus.menu_1()

    user_choice = validate_input()

    # ⬇️Add tasks — give it a title and a priority (low/medium/high).
    if user_choice == False:
        continue                       #⬅️ if False, skip everything below, go re-print the menu and ask again
    elif user_choice == 1:

        if len(all_tasks) < 20:

            title_input = input("Enter task title:\n")
            priority_input = input("Enter one of the following choices (low/medium/high priority):\n").lower()
            task_type = int(input("Task type — (1) One-time or (2) Recurring?:\n"))

            if priority_input != "" and priority_input not in VALID_PRIORITIES:      #⬅️ Checks 4 input in 'priority_input' other than empty strng & those allowed.
                print("That is not a valid option.")
                priority_input = ""

            if task_type == 1:
                if priority_input == "":                                             #⬅️ if empty strng input in 'priority_input', 'Task' class then assigns default "medium".
                    one_time_task = Task(title=title_input)
                else:
                    one_time_task = Task(title=title_input, priority=priority_input)      #⬅️ If 'priority_input' not empty strng & matches allowed options, then it is assigned to priority parameter in 'Task' class.
                all_tasks.append(one_time_task)
            elif task_type == 2:
                frequency = input("Enter 'D' for Daily, or 'W' for Weekly:\n").lower()
                if priority_input == "":                                            #⬅️ if empty strng input in 'priority_input', 'RecurringTask' class then assigns default "medium".
                    habitual_task = RecurringTask(title=title_input, frequency=frequency)
                else:
                    habitual_task = RecurringTask(title=title_input, priority=priority_input, frequency=frequency)
                all_tasks.append(habitual_task)
        else:
            print(f"You have reached your limit of {MAX_TASKS} tasks. Complete some tasks before adding more.")
    elif user_choice == 2:
        if len(all_tasks) > 0:
            while True:
                menus.menu_2()
                view_tasks_type = validate_input()
                if view_tasks_type == False:
                    continue
                elif view_tasks_type == 1:
                    for task in all_tasks:
                        print(task.describe())
                elif view_tasks_type == 2:
                    filter_tasks(tasks=all_tasks, done=True)
                elif view_tasks_type == 3:
                    filter_tasks(tasks=all_tasks)
                elif view_tasks_type == 4:
                    sorted_by_priority = sort_tasks(
                        tasks= all_tasks,                                           #⬅️ all task objects list.
                        key_func=lambda task: PRIORITY_WEIGHTS[task.priority],      #⬅️[1] lambda: temporary func. returns value of the priority attribute of each task object.
                        reverse=True                                                
                    )
                    print(sorted_by_priority)
                else:
                    break
        else:
            print("You currently have no tasks to show.")
    elif user_choice == 3:
        title_input = input("Enter task title:\n")
        for task in all_tasks:
            if task.title == title_input:
                if task.done == False:
                    task.done = True
                    mark_done()
                else:
                    print(f"You've already completed this task: {task.title}")
        pass
    elif user_choice == 4:
        menus.menu_3()
        view_stat_type = validate_input()                                           #⚠️ Currently here.

        if view_stat_type == False:
            continue
        elif view_stat_type == 1:
            print_summary(all_tasks=all_tasks)
        elif view_stat_type == 2:
            incomplete_tasks = filter_tasks(tasks=all_tasks)
            for task in incomplete_tasks[:3]:                                     #⬅️ Accesses & prints ur next 3 incomplete tasks.
                print(task.describe())
        elif view_stat_type == 3:
            completed_tasks = filter_tasks(tasks=all_tasks, done=True)
            for task in completed_tasks[-5:]:                              #⬅️ Accesses & prints ur last 5 completed tasks. Counts down -5 from the end of list.
                print(task.describe())

    elif user_choice == 5:
        break
    else:
        print(f"{user_choice} is not a option. Try again.")

# Saved to github....


# NOTE:
#[1] lambda: a small, unnamed function in a single line, right where you need it, 
# instead of writing a full def block somewhere else in your file and giving it a name.
#   - Are meant to stay small and disposable.
#   - Almost always as a quick, throwaway function passed into another function that expects 
#     one — situations where writing a full named def elsewhere would be overkill for something 
#     used exactly once, right here.
#   - There's no explicit return keyword, because a lambda is always just one expression that gets 
#     evaluated and handed back. 
#   - You typically don't even store it in a variable; you just write it directly at the spot where 
#     a function is expected as an argument.
