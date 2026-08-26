# Here, all of the main task classes will exist.


class Task:
    def __init__(self, title, priority = "medium", done = False):
        self.title = title
        self.priority = priority
        self.done = done
        self.count = 0

    def mark_done(self):
        """Marks task as completed."""
        self.done = True

    def describe(self):
        """Returns a formatted string using the object's attributes"""
        return f"Task: {self.title}| Priority: {self.priority}| Completed: {self.done}"