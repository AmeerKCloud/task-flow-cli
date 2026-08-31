# module: helper functions, constants

VALID_PRIORITIES = ("low", "medium", "high")

PRIORITY_WEIGHTS = {
    "low" : 1,
    "medium" : 2,
    "high" : 3,
    }
class Menu:
    def menu_1(self):
        print("\n" * 20)
        print("""
        === TaskFlow ===
        1. Add task
        2. List tasks
        3. Mark task done
        4. Show stats
        5. Exit
        """)
        