# Here, all of the main task classes will exist.


class Task:
    def __init__(self, title, priority = "medium", done = False):
        self.title = title
        self.priority = priority
        self.done = done

    def mark_done(self):
        self.done = True

    def describe(self):
        return f"{self.title}"