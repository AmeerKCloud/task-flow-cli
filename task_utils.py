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
    """Returns tasks matching a status."""
    pass


def sort_tasks():
    """Accepts a function (e.g. lambda t: PRIORITY_WEIGHTS[t.priority]) to sort by."""
    pass

class Menu:
    def menu_1(self):
        print("""
        === TaskFlow ===
        1. Add task
        2. List tasks
        3. Mark task done
        4. Show stats
        5. Exit
        """)
        