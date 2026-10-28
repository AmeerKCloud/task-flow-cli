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
from task_utils import PrintMenu, VALID_PRIORITIES, PRIORITY_WEIGHTS, filter_tasks, sort_tasks, get_stats, format_task_line, shuffle_tasks, validate_input, validate_priority
import os

print_menus = PrintMenu()

MAX_TASKS = 20      #⬅️ Blocks "Add task" once the 'all_tasks' list is full

#⬇️ Store tasks as a list of Task/RecurringTask objects.
stored_data_tasks = []

#⬇️ Store tasks that user added just now, but did not save to data.txt.
new_tasks = []

#⬇️ Store all tasks as a list of Task/RecurringTask objects inside program.
all_tasks = []

total_completed = 0

#⬇️ Main 'main.py' program from here onwards:

def print_summary(all_tasks):
    """Recieves the 'all_tasks' list; calculates & prints the # & % 
    of tasks completed from the current list of task objects."""

    completed_count, percent_done, streak_score, is_even = get_stats(all_tasks=all_tasks)

    print(f"# of tasks completed: {completed_count}")
    print(f"Percentage completed: {percent_done}")
    print(f"Your streak score: {streak_score}")
    print(f"Is amount completed even? {completed_count}")

def mark_done():
    """
    Increments 'total_completed' every time a task is marked done.
    Accumulates & tracks total # of tasks completed over the life 
    of this program.
    """
    global total_completed
    total_completed += 1
    return total_completed


if os.path.exists("data.txt"):                  #⬅️ Checks for the data files existence; prevents 'FileNotFoundError' on first time program run, b4 any data file created.
    with open(file="data.txt") as f:
        for line in f:
            clean_string = line.strip()                 #⬅️ Removes any spaces on either side of, & new lines from, a string.
            string_list = clean_string.split("|")       #⬅️ Splits a string into a several strings list at a given character, here '|'.
            if string_list[0] == "one":
                if string_list[3] == "True":
                    one_time_task = Task(title=string_list[1], priority=string_list[2], done=True)
                else:
                    one_time_task = Task(title=string_list[1], priority=string_list[2])
                stored_data_tasks.append(one_time_task)
                # all_tasks.append(one_time_task)
            else:
                if string_list[3] == "True":
                    habitual_task = RecurringTask(title=string_list[1], priority=string_list[2], done=True, frequency=string_list[4])
                else:
                    habitual_task = RecurringTask(title=string_list[1], priority=string_list[2], frequency=string_list[4])
                stored_data_tasks.append(habitual_task)
                # all_tasks.append(habitual_task)

        with open(file="data.txt", mode="w") as f:      #⬅️ Clears file after extracting all stored data into the task-objects lists.
            pass

    all_tasks = stored_data_tasks          #⬅️ Combine the two separate task object lists into the main program list.


while True:

    print_menus.menu_1()

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
                new_tasks.append(one_time_task)
            elif task_type == 2:
                frequency = input("Enter 'D' for Daily, or 'W' for Weekly:\n").lower()
                if priority_input == "":                                            #⬅️ if empty strng input in 'priority_input', 'RecurringTask' class then assigns default "medium".
                    habitual_task = RecurringTask(title=title_input, frequency=frequency)
                else:
                    habitual_task = RecurringTask(title=title_input, priority=priority_input, frequency=frequency)
                new_tasks.append(habitual_task)

            all_tasks.extend(new_tasks)                 #⬅️ '.extend()' method extends a list with the targeted list's individual list items.
        else:
            print(f"You have reached your limit of {MAX_TASKS} pending tasks. Complete some tasks before adding more.")

    elif user_choice == 2:
        if all_tasks:
            while True:
                print_menus.menu_2()
                view_tasks_type = validate_input()

                if view_tasks_type == False:
                    continue
                elif view_tasks_type == 1:                      #⚠️BUG2: Currently here. Only tasks in all_tasks get printed, not 'all_tasks'.
                    for index in range(len(all_tasks)):
                        print(format_task_line(task=all_tasks[index], task_index=index))

                elif view_tasks_type == 2:
                    done_tasks = filter_tasks(tasks=all_tasks, done=True)   #⬅️ 'done_tasks' list contains all tasks marked 'done'.
                    for index in range(len(done_tasks)):
                        print(format_task_line(task=done_tasks[index], task_index=index))
                elif view_tasks_type == 3:
                    incomplete_tasks = filter_tasks(tasks=all_tasks)
                    for index, task in enumerate(incomplete_tasks):                             #⬅️[3] 'enumerate()' is more effecient than 'range(len(my_list))'
                        print(format_task_line(task=task, task_index=index))
                elif view_tasks_type == 4:
                    sorted_by_priority = sort_tasks(
                        tasks= all_tasks,                                           #⬅️ all task objects list.
                        key_func=lambda task: PRIORITY_WEIGHTS[task.priority],      #⬅️[1] lambda: temporary func. returns value of the priority attribute of each task object.
                        reverse=True                                                
                    )
                    print(sorted_by_priority)
                elif view_tasks_type == 5:
                    shuffle_tasks(tasks=all_tasks)
                    print("Your tasks have been shuffled.")
                else:
                    break
        else:
            print("You currently have no tasks to show.")
    elif user_choice == 3:
        if all_tasks:
            title_input = input("Enter task title:\n")
            for task in all_tasks:
                if task.title == title_input:
                    if task.done == False:
                        task.done = True
                        mark_done()
                    else:
                        print(f"You've already completed this task: {task.title}")
        else:
            print("You currently have no tasks.")
    elif user_choice == 4:
        print_menus.menu_3()
        view_stat_type = validate_input()

        if view_stat_type == False:
            continue
        elif view_stat_type == 1:
            print_summary(all_tasks=all_tasks)
        elif view_stat_type == 2:
            incomplete_tasks = filter_tasks(tasks=all_tasks)
            for index, task in enumerate(incomplete_tasks[:3]):                          #⬅️ Accesses & prints ur next 3 incomplete tasks. Starts @ 0, counts upwards until 3, excluding 3.
                print(format_task_line(task=task, task_index=index))
        elif view_stat_type == 3:
            completed_tasks = filter_tasks(tasks=all_tasks, done=True)
            for index, task in enumerate(completed_tasks[-5:]):                          #⬅️ Accesses & prints ur last 5 completed tasks. Counts down backwads -5 from the end of list.
                print(format_task_line(task=task, task_index=index))

    elif user_choice == 5:
        if new_tasks:
            if os.path.exists("data.txt") and stored_data_tasks:          #⬅️ If the data file already exists & data stores in list, read the file.
                for task in new_tasks:
                    counter = 0
                    for stored_task in stored_data_tasks:                #⬅️ For task object in stored tasks in data file list.
                        if task.title == stored_task.title:        #⬅️ If task-object title matches a stored-task-object title already stored in data.txt file...
                            counter += 1                           #⬅️ Than counter increases.

                    if counter > 0:
                        print(f"Task '{task.title}' already exists. NOT added to data file")
                    else:
                        stored_data_tasks.append(task)

                with open(file="data.txt", mode="w") as f:            #⬅️ mode="w" means write. BUG#1a: Resolved, see notes.
                    for stored_task in stored_data_tasks:
                        if isinstance(stored_task, RecurringTask):                   #⬅️[4] isinstance() checks whether an object is an instance of a given class (or type); returns True or False.
                            marker = "recurring"
                            frequency = stored_task.frequency
                        else:
                            marker = "one"
                            frequency = ""
                        string_list = [marker, stored_task.title, stored_task.priority, str(stored_task.done), frequency]
                        data_string = "|".join(string_list)
                        f.write(data_string + "\n")
            else:
                with open(file="data.txt", mode="w") as f:               #⬅️ Else If the data file doesnt already exist, write/create the file.
                    for task in new_tasks:
                        if isinstance(task, RecurringTask):                   #⬅️[4] isinstance() checks whether an object is an instance of a given class (or type); returns True or False.
                            marker = "recurring"
                            frequency = task.frequency                   #⬅️ 'Daily' or 'Weekly' frequency.
                        else:
                            marker = "one"
                            frequency = ""
                        string_list = [marker, task.title, task.priority, str(task.done), frequency]
                        data_string = "|".join(string_list)
                        f.write(data_string + "\n")
            break
        else:
            with open(file="data.txt", mode="w") as f:            #BUG#1a: Resolved, see notes.
                for stored_task in stored_data_tasks:
                    if isinstance(stored_task, RecurringTask):
                        marker = "recurring"
                        frequency = stored_task.frequency
                    else:
                        marker = "one"
                        frequency = ""
                    string_list = [marker, stored_task.title, stored_task.priority, str(stored_task.done), frequency]
                    data_string = "|".join(string_list)
                    f.write(data_string + "\n")
                print("No new changes made.")
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

#[2] range(len(my_list)): len() gives you the count (eg 4), and then range() takes that count & converts 
# it into a sequence of valid indices (0 through 3) — because range(4) always means "give me 4 numbers, starting from 0."

#[3] enumerate(): It does automatically behind the scenes what range(len(my_list)) do.

#[4] isinstance() is a built-in function that checks whether an object is an instance of a given class (or type). It returns True or False.


# ⚠️BUG1a FIXED: 'with open(..., mode="w")' should be out of loop otherwise previous line in 'data.txt' will be erased & overwritten by next 
# task-object everytime the loop runs & the file is opened.
# - Solution: open once b4 loop, then every loop writes the new task data line.

# ⚠️BUG3: Whenever i add a new task, then shuffle the 'all_tasks' list, and then select option 5 'exit' in the main menu, the program thinks 
# the new task is an old task that already exists in data.txt and thus triggers the print statement 'Task 'climbing' already exists. NOT added to data file'. 
# Find out why this is happening and fix it.


#_______________________ Reserve Code ________________________:

