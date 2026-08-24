# entry point, menu loop, user I/O

# A CLI app where users add tasks, mark them done, track recurring habits, and 
# save/load their data to a file — with a small stats report at the end

class Task:
    def __init__(self, title, priority):
        self.title = title
        if priority == "":
            self.priority = "medium"
        else:
            self.priority = priority
        self.done = False