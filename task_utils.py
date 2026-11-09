# module: helper functions, constants

import random

VALID_PRIORITIES = ("low", "medium", "high")        #⬅️ Constant variable: tuple containing priority weights.

#⬇️ Constant variable: dict. containing priority weights as keys with # values for easy processing in main.py program when filtering by priority.
PRIORITY_WEIGHTS = {
    "low" : 1,
    "medium" : 2,
    "high" : 3,
    }


def validate_priority():
    """Enter function explanation here."""
    pass


def filter_tasks(tasks, done=False):
    """Returns a list of task objects matching a status, ie done = True or False."""
    matching_tasks = []
    for task in tasks:
        if task.done == done:
            matching_tasks.append(task)
    return matching_tasks


def sort_tasks(tasks, key_func, reverse=False):
    """Accepts a function (e.g. lambda t: PRIORITY_WEIGHTS[t.priority]) to sort by."""
    return sorted(tasks, key=key_func, reverse=reverse)

def get_stats(all_tasks):
    """Return the stats as a tuple (completed_count, percent_done, streak_score, is_even)."""
    total_tasks = len(all_tasks)
    completed_count = 0
    for task in all_tasks:
        if task.done == True:
            completed_count += 1
    streak_score = 2 ** completed_count
    is_even = completed_count % 2 == 0
    percent_done = round((completed_count / total_tasks) * 100, 2)
    return (completed_count, percent_done, streak_score, is_even)

def validate_input():
    """Catches any non-numerical or blank user entries."""
    try:
        user_input = int(input("Choose one numerical option:\n"))
        return user_input
    except ValueError:
        print("Invalid entry. Cannot leave field blank or enter non-numerical entry")
        return False

def format_task_line(task, task_index):
    """takes a task and produces one clean, ready-to-print line of text describing it 
    — something you'd call from multiple places in main.py (List tasks, Show stats' 
    "next 3" preview, etc.) instead of writing the same formatting/f-string logic 
    over and over in each menu option."""

    if task.done == False:
        return f"[ ] {task_index + 1}. {task.describe()}"
    else:
        return f"[X] {task_index + 1}. {task.describe()}"

def random_motivational_quote():
    rand_quotes = ["You got this!!", "One step at a time!", "Do better!", "Don't quit now!", "You're almost there!", "Quitting is for losers"]
    rand_quote = random.choice(rand_quotes)
    print(rand_quote)

def shuffle_tasks(tasks):
    random.shuffle(tasks)

def file_handling(file_name, task_list, task_class, mode="r",):         #⚠️ Has not been imported into main.py yet.
    """Handles the file by either reading or writing to it."""
    with open(file=file_name, mode=mode) as f:            #⬅️ mode="w" means write. BUG#1a: Resolved, see notes.
        for stored_task in task_list:
            if isinstance(stored_task, task_class):                   #⬅️[4] isinstance() checks whether an object is an instance of a given class (or type); returns True or False.
                marker = "recurring"
                frequency = stored_task.frequency
            else:
                marker = "one"
                frequency = ""
            string_list = [marker, stored_task.title, stored_task.priority, str(stored_task.done), frequency]
            data_string = "|".join(string_list)
            f.write(data_string + "\n")

class PrintMenu:

    #⬇️ All functions without inputs.
    def menu_1(self):
        """The main menu."""
        print("""
        === TaskFlow ===
        1. Add task
        2. List tasks
        3. Mark task done
        4. Show stats
        5. Exit
        """)

    def menu_2(self):
        """2nd menu: Lists tasks."""
        print("""
        === 🌸 ===
        1. View all tasks
        2. View completed tasks only
        3. View incomplete tasks only
        4. Sort by priority
        5. Shuffle my tasks
        6. Return to main menu
        """)

    def menu_3(self):
        """3rd menu: shows stats."""
        print("""
        === ⭐ ===
        1. View summary of all tasks
        2. View your next 3 tasks
        3. View your last 5 completed tasks
        4. Sort by priority
        5. Return to main menu
        """)