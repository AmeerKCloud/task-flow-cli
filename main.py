# entry point, menu loop, user I/O

# ______________ Objective:
# A CLI app where users add tasks, mark them done, track recurring habits, and 
# save/load their data to a file — with a small stats report at the end

# ______________ Core functionalities
# Add tasks — give it a title and a priority (low/medium/high).
# Add recurring tasks — same as above, but tagged with a frequency (daily/weekly), so they behave a little differently from a normal one-off task.
# List tasks — see everything, or just what's pending vs. completed.
# Mark tasks done — updates the task's internal state.
# View stats — completion percentage, counts, and a couple of small computed numbers.
# Random extras — a motivational quote, or a shuffle feature to "surprise" you with what to work on next.
# Persistence — saves to a file on exit, loads from it on startup, so your list survives between sessions.


# ⬇️ Part of the 'Add Tasks' functionality. To be transferred to a module once completed.
class Task:
    def __init__(self, title, priority):
        self.title = title
        if priority == "":
            self.priority = "medium"
        else:
            self.priority = priority
        self.done = False

    def mark_done(self):
        self.done = True

    def describe(self):
        return f"{self.title}"



#⬇️ Main 'main.py' program:

def menu_options():
    options = {
        1 : "Add task",
        2 : "List tasks",
        3 : "Mark task done",
        4 : "Show stats",
        5 : "Exit",
    }

    return options

print("\n" * 20)
print("=== TaskFlow ===")

for key, value in menu_options().items():
    print(f"{key}. {value}")

try:
    user_choice = int(input("Choose one numerical option:\n"))
except ValueError:
    print("Invalid entry. Cannot leave field blank or enter non-numerical entry")


# ⬇️ Add tasks — give it a title and a priority (low/medium/high).
for key in menu_options():
    if user_choice == key:
        Task.

# Saved to github.