# module: helper functions, constants

VALID_PRIORITIES = ("low", "medium", "high")

PRIORITY_WEIGHTS = {
    "low" : 1,
    "medium" : 2,
    "high" : 3,
    }


def validate_priority():
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
    try:
        user_input = int(input("Choose one numerical option:\n"))
        return user_input
    except ValueError:
        print("Invalid entry. Cannot leave field blank or enter non-numerical entry")
        return False

class Menu:
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
        5. Return to main menu
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