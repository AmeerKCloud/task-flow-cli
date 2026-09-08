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
    """Returns tasks matching a status, ie done = True or False."""
    for task in tasks:
        if task.done == done:
            print(task.describe())
    pass


def sort_tasks(tasks, key_func, reverse=False):
    """Accepts a function (e.g. lambda t: PRIORITY_WEIGHTS[t.priority]) to sort by."""
    return sorted(tasks, key=key_func, reverse=reverse)


def validate_input():
    try:
        user_input = int(input("Choose one numerical option:\n"))
        return user_input
    except ValueError:
        print("Invalid entry. Cannot leave field blank or enter non-numerical entry")
        return False

class Menu:
    def menu_1(self):
        print("""
        === TaskFlow ===
        1. Add task
        2. List tasks
        3. Mark task done
        4. Show stats
        5. Sort by priority
        6. Exit
        """)

    def menu_2(self):
        print("""
        === 🌸 ===
        1. View all tasks
        2. View completed tasks only
        3. View incomplete tasks only
        4. Sort by priority
        5. Return to main menu
        """)
