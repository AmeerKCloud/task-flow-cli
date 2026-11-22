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
from task_utils import PrintMenu, create_task, filter_tasks, sort_priority, get_stats, format_task_line, print_task, shuffle_tasks, validate_input, validate_priority, file_handling
import os

print_menus = PrintMenu()

MAX_TASKS = 20      #⬅️ Blocks "Add task" once the 'all_tasks' list is full

#⬇️ Loads & holds all tasks currently stored within 'data.txt'.
stored_data_tasks = []

#⬇️ Store all tasks as a list of Task/RecurringTask objects inside program.
all_tasks = []

total_completed = 0         #⬅️ Tally of total number of tasks completed anytime a task is marked done.

#⬇️ Main 'main.py' program from here onwards:

def print_summary(all_tasks):
    """Recieves the 'all_tasks' list; calculates & prints the # & % 
    of tasks completed from the current list of task objects as well as the odd or even."""

    completed_count, percent_done, streak_score, is_even = get_stats(all_tasks=all_tasks)   #⬅️ 'is_even' contains bool True or False based on if amount_completed is even or ordd num.

    print(f"# of tasks completed: {completed_count}")
    print(f"Percentage completed: {percent_done}")
    print(f"Your streak score: {streak_score}")
    print(f"Is amount completed even? {is_even}")

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
            else:
                if string_list[3] == "True":
                    habitual_task = RecurringTask(title=string_list[1], priority=string_list[2], done=True, frequency=string_list[4])
                else:
                    habitual_task = RecurringTask(title=string_list[1], priority=string_list[2], frequency=string_list[4])
                stored_data_tasks.append(habitual_task)

        all_tasks = stored_data_tasks.copy()        #⬅️ '.copy()' returns a duplicate of the original list being copied & creates new list. Original list not affected by any changes to new list.
        stored_length = len(stored_data_tasks)      #⬅️ This is the total # of all task objects currently read from 'data.txt' file.
else:
    stored_length = 0

#⬇️ Part 2 — Menu & User Interaction: 4. Build while loop menu that keeps running until user exits [While Loop]
while True:

    print_menus.menu_1()

    menu_1_user_choice = validate_input(input("Choose one numerical option:\n"), print_menus.menu_1_choices_numbered)

    #⬇️ Part 2 — Menu & User Interaction: 5. Inside the loop, use if/elif/else to branch on the user's menu choice. [If/Elif/Else, Conditionals]
    if menu_1_user_choice == False:
        continue                       #⬅️ 'continue': if False, skip everything below, go re-print the menu and ask again
    elif menu_1_user_choice == 1:

        if len(all_tasks) < 20:

            #⬇️ Part 2 — Menu & User Interaction: 6. Use input() to collect task title, priority, and frequency. [User Inputs]
            title_input = input("Enter task title:\n").lower().strip()
            if not title_input or '|' in title_input:
                print("Cannot leave task title field blank or use '|' in title. Try again.")
                continue
            priority_input = input("Enter one of the following (low/medium/high priority):\n").strip().lower()  #⬅️ '.strip()' removes spaces.

            if priority_input != "":                                #⬅️ If priority input is not an empty string, then this code bloc gets triggered.
                if not validate_priority(priority_input):
                    print("Priority must be low, medium, or high")
                    continue                                            #⬅️ 'continue' takes back to main menu.

            while True:
                print_menus.menu_1a()
                task_type = validate_input(input("Choose one numerical option:\n"), print_menus.menu_1a_choices_numbered)

                if not task_type:
                    continue
                elif task_type == 1:
                    one_time_task = create_task(title = title_input, priority = priority_input)      #⬅️ If 'priority_input' not empty strng & matches allowed options, then it is assigned to priority parameter in 'Task' class.
                    all_tasks.append(one_time_task)
                    break
                elif task_type == 2:
                    frequency = input("Enter 'D' for Daily, or 'W' for Weekly:\n").lower().strip()
                    habitual_task = create_task(title = title_input, priority = priority_input, frequency = frequency)
                    all_tasks.append(habitual_task)
                    break

        else:
            print(f"You have reached your limit of {MAX_TASKS} pending tasks. Complete some tasks before adding more.")

    elif menu_1_user_choice == 2:
        if all_tasks:
            while True:
                print_menus.menu_2()
                view_tasks_type = validate_input(input("Choose one numerical option:\n"), print_menus.menu_2_choices_numbered)

                if view_tasks_type == False:
                    continue
                elif view_tasks_type == 1:

                    #⬇️ Part 2 — Menu & User Interaction: 7. Print a formatted task list using a for loop & f-strings. [For Loop, User Outputs, String Manipulation]
                    for index in range(len(all_tasks)):
                        print_task(task=all_tasks[index], task_index=index)

                elif view_tasks_type == 2:
                    done_tasks = filter_tasks(tasks=all_tasks, done=True)   #⬅️ 'done_tasks' list contains all tasks marked 'done'.
                    for index in range(len(done_tasks)):
                        print_task(task=done_tasks[index], task_index=index)
                elif view_tasks_type == 3:
                    incomplete_tasks = filter_tasks(tasks=all_tasks)
                    for index, task in enumerate(incomplete_tasks):                             #⬅️[3] 'enumerate()' is more effecient than 'range(len(my_list))'
                        print(format_task_line(task=task, task_index=index))
                elif view_tasks_type == 4:
                    while True:
                        print_menus.menu_2a()
                        priority_order = validate_input(input("Choose one numerical option:\n"), print_menus.menu_2a_choices_numbered)

                        if not priority_order:
                            continue                                                                #⚠️ Currently here.

                        if priority_order == 1:
                            sorted_by_priority = sort_priority(all_tasks=all_tasks, reverse=True)
                            for index in range(len(sorted_by_priority)):
                                print_task(task=sorted_by_priority[index], task_index=index)
                        elif priority_order == 2:
                            sorted_by_priority = sort_priority(all_tasks=all_tasks)
                            for index in range(len(sorted_by_priority)):
                                print_task(task=sorted_by_priority[index], task_index=index)
                        else:
                            break
                elif view_tasks_type == 5:
                    shuffle_tasks(tasks=all_tasks)
                    print("Your tasks have been shuffled.")
                else:
                    break
        else:
            print("You currently have no tasks to show.")
    elif menu_1_user_choice == 3:
        if all_tasks:
            title_input = input("Enter task title:\n").lower().strip()
            priority_input = input("Enter one of the following (low/medium/high priority):\n").lower().strip()
            frequency_input = input("Enter 'D' for Daily, or 'W' for Weekly:\n").lower().strip()
            count_down = len(all_tasks)
            for task in all_tasks:
                if frequency_input:
                    if task.title == title_input and task.priority == priority_input and task.frequency == frequency_input:
                        if task.done == False:
                            task.done = True
                            mark_done()
                            print(f"Hurray! 🥳 You just completed the following task :{task.title}, {task.priority}, {task.frequency}! 🎉")
                        else:
                            print(f"You've already completed this task.")
                    else:
                        count_down -= 1         #⬅️ If the task doesnt match, counter counts down.
                else:
                    """This 'else' should target task objects without a 'frequency'' attribute if user chooses to leave the frequency field empty."""
                    if task.title == title_input and task.priority == priority_input:
                        if task.done == False:
                            task.done = True
                            mark_done()
                            print(f"Hurray! 🥳 You just completed the following task :{task.title}, {task.priority}, one time task! 🎉")
                        else:
                            print(f"You've already completed this task.")
                    else:
                        count_down -= 1

            if count_down == 0:
                print("Sorry. No task matching those requirements exists.")       #⚠️ Currently here. Find out how to make it print after checking all objects & then printing.
        else:
            print("You currently have no tasks.")
    elif menu_1_user_choice == 4:
        if all_tasks:
            while True:
                print_menus.menu_3()
                view_stat_type = validate_input(input("Choose one numerical option:\n"), print_menus.menu_3_choices_numbered)

                if view_stat_type == False:
                    continue
                elif view_stat_type == 1:
                    print_summary(all_tasks=all_tasks)
                elif view_stat_type == 2:
                    incomplete_tasks = filter_tasks(tasks=all_tasks)
                    for index, task in enumerate(incomplete_tasks[:3]):              #⬅️ Accesses & prints ur next 3 incomplete tasks. Starts @ 0, counts upwards until 3, excluding 3.
                        print(format_task_line(task=task, task_index=index))
                elif view_stat_type == 3:
                    completed_tasks = filter_tasks(tasks=all_tasks, done=True)
                    for index, task in enumerate(completed_tasks[-5:]):              #⬅️ Accesses & prints ur last 5 completed tasks. Counts down backwads -5 from the end of list.
                        print(format_task_line(task=task, task_index=index))
                else:
                    break
        else:
            print("You currently have no tasks.")

    elif menu_1_user_choice == 5:

        with open(file="data.txt", mode="w") as f:      #⬅️ Clears file 'data.txt' b4 writing extracted/new data in order to prevent duplicate data.
            pass

        if len(all_tasks) > stored_length:                #⬅️ If the length of all_tasks is greater than the length of stored_tasks, this means new tasks were added.
            counter = 0
            for stored_task in stored_data_tasks:     #⬅️ Uses each already stored task object as standard to compare all task objects in 'all_tasks' list.
                for task in all_tasks:
                    if task.frequency:
                        if stored_task.title == task.title and stored_task.priority == task.priority and stored_task.frequency == task.frequency:
                            counter += 1
                            if counter > 1:                                                            #⬅️ If counter exceeds 1 means there's duplicate of task object, remove it.
                                print(f"A task with those attributes already exists. NOT added to data file")
                                all_tasks.remove(task)
                    else:
                        if stored_task.title == task.title and stored_task.priority == task.priority:
                            counter += 1
                            if counter > 1:                                                            #⬅️ If counter exceeds 1 means there's duplicate of task object, remove it.
                                print(f"A task with those attributes already exists. NOT added to data file")
                                all_tasks.remove(task)

                counter = 0                         #⬅️ Counter gets reset to 0 for next iteration.

            file_handling(file_name="data.txt", task_list=all_tasks, task_class=RecurringTask, mode="w")
            break
        else:
            """If length of 'all_tasks' list has not increased from length of 'stored_length' list, 
            then only rewrite back what already was stored"""
            file_handling(file_name="data.txt", task_list=all_tasks, task_class=RecurringTask, mode="w")
            print("No new changes made.")
            break                                   #⬅️ Breaks programs main while-loop to exit program
    else:
        print(f"{menu_1_user_choice} is not a option. Try again.")

# Saved to github......

# TODO: Whats left is (✅=fixed/completed, ⚠️=not clear/is it necessary?, ❌=to be fixed/completed):
# Bugs found by Claude, worst first
#✅ 1 - Add task crashes every time. main.py line 106 calls validate_input() with only one argument, but the function requires two 
#     (the prompt and the list of valid choices). Python raises a TypeError as soon as the user reaches "Task type". If your local 
#     copy differs from what you uploaded, this may already be fixed.
#✅ 2 - Stats summary crashes when there are no tasks. It divides by zero.
#✅ 3 - "Return to main menu" doesn't work in the sort submenu. Choosing option 3 prints the list sorted lowest to highest and keeps 
#     you in the menu. The only way out is closing the program.
#✅ 4 - "Return to main menu" doesn't work in the stats menu either. Option 4 has no branch, so the menu just re-prompts.
#⚠️ 5 - A blank line in data.txt crashes startup with an IndexError.
#✅ 6 - A title containing | corrupts the save file. I saved a task titled a|b. It reloaded with priority b, and sorting then crashed 
#     with a KeyError. A hand-edited bad priority such as urgent crashes the sort the same way.
#✅ 7 - Blank task titles are accepted.
#⚠️ 8 - A blank frequency on a recurring task silently creates a one-time task. Frequency x is also accepted and shows as "unknown".
#❌ 9 - Mark done gives poor feedback. It prints no confirmation and no "not found" message. It also marks every task that shares the title.
#❌ 10 - "No new changes made." prints even when you marked tasks done, although those changes are saved.
#❌ 11 - Duplicate titles are handled inconsistently. A new task matching a stored title shows in your list all session, then is silently 
#      dropped on exit. Two new tasks with the same title both get saved.
#❌ 12 - create_task() raises a KeyError if priority is omitted, although its docstring says it falls back to the default.

# IMPORTANT: Concepts I need to expand on/ practice more:
# - lambda
# - .count() method
# - enumerate() class

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

# ⚠️BUG3 RESOLVED: Whenever i add a new task, then shuffle the 'all_tasks' list, and then select option 5 'exit' in the main menu, the program thinks 
# the new task is an old task that already exists in data.txt and thus triggers the print statement 'Task 'climbing' already exists. NOT added to data file'. 
# Find out why this is happening and fix it.
# - 'all_tasks = stored_data_tasks' ❌: This doesn't copy the list. It gives the same list a second name, so anything added to all_tasks is also in stored_data_tasks
#   > 1: You add a task, such as climbing, and it goes into new_tasks.
#   > 2: Line 124 extends all_tasks with new_tasks, which also puts climbing in stored_data_tasks.
#   > 3: When you exit, lines 194-198 check each new task against stored_data_tasks. 
#   > 4: climbing finds itself there, so counter goes above 0 and the "already exists" message prints.
#       - Why the task still gets saved:
#           > The message is right that line 203 skips the append, but the task is already in stored_data_tasks from step 2. 
#             The loop at line 206 then writes everything in that list to data.txt, including climbing.
# - 'all_tasks = stored_data_tasks.copy()' ✅: --> The fix:
#   > Assign a copy of stored tasks to the all_task list using '.copy()' mthod without altering the original 'stored_data_tasks'.
#   > stored_data_tasks then only contains what was loaded from the file, so the duplicate check works and a real duplicate won't 
#     be saved. Marking a task done still works because both lists point to the same task objects.


#_______________________ Reserve Code 1 ________________________:

    # elif user_choice == 5:
    #     if new_tasks:
    #         if os.path.exists("data.txt") and stored_data_tasks:          #⬅️ If the data file already exists & data stores in list, read the file.
    #             for task in new_tasks:
    #                 counter = 0
    #                 for stored_task in stored_data_tasks:                #⬅️ For task object in stored tasks in data file list.
    #                     if task.title == stored_task.title:        #⬅️ If task-object title matches a stored-task-object title already stored in data.txt file...
    #                         counter += 1                           #⬅️ Than counter increases.

    #                 if counter > 0:
    #                     print(f"Task '{task.title}' already exists. NOT added to data file")
    #                 else:
    #                     stored_data_tasks.append(task)

    #             with open(file="data.txt", mode="w") as f:            #⬅️ mode="w" means write. BUG#1a: Resolved, see notes.
    #                 for stored_task in stored_data_tasks:
    #                     if isinstance(stored_task, RecurringTask):                   #⬅️[4] isinstance() checks whether an object is an instance of a given class (or type); returns True or False.
    #                         marker = "recurring"
    #                         frequency = stored_task.frequency
    #                     else:
    #                         marker = "one"
    #                         frequency = ""
    #                     string_list = [marker, stored_task.title, stored_task.priority, str(stored_task.done), frequency]
    #                     data_string = "|".join(string_list)
    #                     f.write(data_string + "\n")
    #         else:
    #             with open(file="data.txt", mode="w") as f:               #⬅️ Else If the data file doesnt already exist, write/create the file.
    #                 for task in new_tasks:
    #                     if isinstance(task, RecurringTask):                   #⬅️[4] isinstance() checks whether an object is an instance of a given class (or type); returns True or False.
    #                         marker = "recurring"
    #                         frequency = task.frequency                   #⬅️ 'Daily' or 'Weekly' frequency.
    #                     else:
    #                         marker = "one"
    #                         frequency = ""
    #                     string_list = [marker, task.title, task.priority, str(task.done), frequency]
    #                     data_string = "|".join(string_list)
    #                     f.write(data_string + "\n")
    #         break
    #     else:
    #         with open(file="data.txt", mode="w") as f:            #BUG#1a: Resolved, see notes.
    #             for stored_task in stored_data_tasks:
    #                 if isinstance(stored_task, RecurringTask):
    #                     marker = "recurring"
    #                     frequency = stored_task.frequency
    #                 else:
    #                     marker = "one"
    #                     frequency = ""
    #                 string_list = [marker, stored_task.title, stored_task.priority, str(stored_task.done), frequency]
    #                 data_string = "|".join(string_list)
    #                 f.write(data_string + "\n")
    #             print("No new changes made.")
    #         break
    # else:
    #     print(f"{user_choice} is not a option. Try again.")



#_______________________ Reserve Code 2 ________________________:

            # if task_type == 1:
            #     if priority_input == "":                                             #⬅️ if empty strng input in 'priority_input', 'Task' class then assigns default "medium".
            #         one_time_task = Task(title=title_input)
            #     else:
            #         one_time_task = Task(title=title_input, priority=priority_input)      #⬅️ If 'priority_input' not empty strng & matches allowed options, then it is assigned to priority parameter in 'Task' class.
            #     all_tasks.append(one_time_task)                                        #⬅️ Add new task object to both 'new' & 'all' tasks lists.
            # elif task_type == 2:
            #     frequency = input("Enter 'D' for Daily, or 'W' for Weekly:\n").lower()
            #     if priority_input == "":                                            #⬅️ if empty strng input in 'priority_input', 'RecurringTask' class then assigns default "medium".
            #         habitual_task = RecurringTask(title=title_input, frequency=frequency)
            #     else:
            #         habitual_task = RecurringTask(title=title_input, priority=priority_input, frequency=frequency)
            #     all_tasks.append(habitual_task)


#_______________________ Reserve Code 3 ________________________:

    # elif user_choice == 5:

    #     if os.path.exists("data.txt"):                        #⬅️⚠️ Is this necessarry? If the data file already exists & data stores in list, read the file.
    #         with open(file="data.txt", mode="w") as f:      #⬅️ Clears file 'data.txt' b4 writing extracted/new data in order to prevent duplicate data.
    #             pass

    #         if len(all_tasks) > stored_length:                #⬅️ If the length of all_tasks is greater than the length of stored_tasks, this means new tasks were added.
    #                 counter = 0
    #                 for stored_task in stored_data_tasks:     #⬅️ Uses each already stored task object as standard to compare all task objects in 'all_tasks' list.
    #                     for task in all_tasks:
    #                         if stored_task.title == task.title:
    #                             counter += 1
    #                             if counter > 1:                                                            #⬅️ If counter exceeds 1 means there's duplicate of task object, remove it.
    #                                 print(f"Task '{task.title}' already exists. NOT added to data file")
    #                                 all_tasks.remove(task)
    #                     counter = 0                         #⬅️ Counter gets reset to 0 for next iteration.

    #                 file_handling(file_name="data.txt", task_list=all_tasks, task_class=RecurringTask, mode="w")
    #         else:
    #             """If length of 'all_tasks' list has not increased from length of 'stored_length' list, 
    #             then only rewrite back what already was stored"""
    #             file_handling(file_name="data.txt", task_list=all_tasks, task_class=RecurringTask, mode="w")
    #             print("No new changes made.")
    #             break                                   #⬅️ Breaks programs main while-loop to exit program

    #     else:
    #         file_handling(file_name="data.txt", task_list=all_tasks, task_class=RecurringTask, mode="w")
    #     break                                                                                               #⬅️ Breaks programs main while-loop to exit program
    # else:
    #     print(f"{user_choice} is not a option. Try again.")