# module: helper functions, constants

from tasks import Task, RecurringTask
import random

VALID_PRIORITIES = ("low", "medium", "high")        #⬅️ Constant variable: tuple containing priority weights.

#⬇️ Part 3 — Data & Logic: 24. Priority weights dict. Used to convert priority text into numbers so tasks can be sorted by actual importance instead of alphabetically. Used inside sort_tasks(). [Dictionaries]
PRIORITY_WEIGHTS = {
    "low" : 1,
    "medium" : 2,
    "high" : 3,
    }

def validate_priority(priority):
    """takes the priority text the user typed and checks it against VALID_PRIORITIES, the tuple ("low", "medium", "high"). 
    It returns True if the text is in there and False if not. It doesn't print anything or ask the user for anything. 
    It only reports yes or no."""

    if priority in VALID_PRIORITIES:
        return True
    else:
        return False

def create_task(**kwargs):                                                  #⬅️ [1]'**kwargs' explained, see notes.
    """Builds a Task or RecurringTask from keyword arguments based on if 
    'frequency' argument is detected.

    A non-empty 'frequency' means RecurringTask; otherwise a plain Task.
    Any key left out (e.g. priority) falls back to the constructor's default.
    """

    priority = kwargs.pop("priority")
    frequency = kwargs.pop("frequency", "")

    if frequency:
        if priority:
            return RecurringTask(frequency=frequency, priority= priority, **kwargs)
        
        return RecurringTask(frequency=frequency, **kwargs)     #⬅️ if 'priority' not exists, then this is read. 'else' can be used here, but not ncessary.

    if priority:                                         #⬅️ if 'frequency' not exists, then this is read. 'else' can be used here, but not ncessary.
        return Task(priority=priority, **kwargs)
    
    return Task(**kwargs)        #⬅️ if 'priority' not exists, then this is read. 'else' can be used here, but not ncessary.

def filter_tasks(tasks, done=False):
    """Returns a list of task objects matching a status, ie done = True or False."""
    matching_tasks = []
    for task in tasks:
        if task.done == done:
            matching_tasks.append(task)
    return matching_tasks

def format_task_line(task, task_index):
    """takes a task & it's index# & produces one clean, ready-to-print line of text describing it 
    — something you'd call from multiple places in main.py (List tasks, Show stats' 
    "next 3" preview, etc.) instead of writing the same formatting/f-string logic 
    over and over in each menu option."""

    if task.done == False:
        return f"[ ] {task_index + 1}. {task.describe()}"
    else:
        return f"[X] {task_index + 1}. {task.describe()}"

#⬇️ Part 7 — Functions Review: 23. At least one function with inputs but no return (e.g., print_task(task)).
def print_task(task, task_index):
    print(format_task_line(task=task, task_index=task_index))

def sort_tasks(tasks, key_func, reverse=False):
    """Accepts a function (e.g. lambda t: PRIORITY_WEIGHTS[t.priority]) to sort by."""
    return sorted(tasks, key=key_func, reverse=reverse)

def sort_priority(**kwargs):
    """Returns a list in either highest-to-lowest priority (or the opposite) 
    order of task objects based on their priority attribute."""
    all_tasks = kwargs.pop("all_tasks")
    reverse = kwargs.pop("reverse", False)

    sorted_by_priority = sort_tasks(
        tasks= all_tasks,                                           #⬅️ all task objects list.
        key_func=lambda task: PRIORITY_WEIGHTS[task.priority],      #⬅️⚠️ This section not completed? [1, 1a] lambda: temporary func. returns value of the priority attribute of each task object.
        reverse=reverse                                                
    )
    return sorted_by_priority

#⬇️ Part 7 — Functions Review: 24. At least one function that returns a value (e.g., get_stats()).
def get_stats(all_tasks):
    """Return the stats as a tuple (completed_count, percent_done, streak_score, is_even)."""
    total_tasks = len(all_tasks)
    completed_count = 0

    for task in all_tasks:
        if task.done == True:
            completed_count += 1

    streak_score = 2 ** completed_count

    if completed_count % 2 == 0:
        is_even = True
    else:
        is_even = False

    percent_done = round((completed_count / total_tasks) * 100, 2)          #⬅️ Concept: Mathematical Operations: Floating Point Numbers
    return (completed_count, percent_done, streak_score, is_even)

def validate_input(input_prompt):
    """Catches any non-numerical or blank user entries."""

    #⬇️ Part 2 — Menu & User Interaction: 7. Wrap all numeric menu input (like "pick task # to complete") in try/except to catch bad input, and validate the value is actually an int using isinstance() before using it. [Try-Except, Type-Checking, Booleans]
    try:
        user_input = int(input_prompt)
        return user_input
    except ValueError:
        print("Invalid entry. Cannot leave field blank, enter non-numerical entry, or enter a choice not provided in the menu")
        return False

def random_motivational_quote():
    rand_quotes = ["You got this!!", "One step at a time!", "Do better!", "Don't quit now!", "You're almost there!", "Quitting is for losers"]
    rand_quote = random.choice(rand_quotes)
    print(rand_quote)

def shuffle_tasks(tasks):
    random.shuffle(tasks)

def file_handling(file_name, task_list, task_class, mode="r",):         #⬅️
    """Handles the file by either reading from or writing to it."""
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

    #⬇️ Part 7 — Functions Review: 22. All functions without parameters.
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

    def menu_2a(self):
        """View by priority"""

        print("""
        === 📏 ===
        1. Highest to lowest
        2. Lowest to highest
        """)

    def menu_3(self):
        """3rd menu: shows stats."""
        print("""
        === ⭐ ===
        1. View summary of all tasks
        2. View your next 3 tasks
        3. View your last 5 completed tasks
        4. Return to main menu
        """)


#___________________________________ NOTES:____________________________________

#[1]`**kwargs` lets a function accept any number of keyword arguments (like `title="Buy milk"`) and collects them into a single dictionary inside the function.