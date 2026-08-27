# This module demonstrates the use of the following python concepts: 
# Classes, Objects, Attributes, Methods, Object State & Instances

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
        return f"Task: {self.title}| Priority: {self.priority}| Completed: {self.done}|"


class RecurringTask(Task):
    def __init__(self, title, priority="medium", done=False, frequency="d"): #⬅️[1] 
        super().__init__(title, priority, done)           #⬅️[1a] Taps into superclass' (Task class) init method, see notes for more.
        self.frequency = frequency                        #⬅️[1b] 

    def describe(self):
        super().describe()

        if self.frequency == "d":
            self.frequency = "daily"
            print(f"Frequency = {self.frequency}")
        elif self.frequency == "w":
            self.frequency == "weekly"
            print(f"Frequency = {self.frequency}")

# NOTE:
#[1]-[1b] To demonstrate class inheritance
#   - [1] Parameters/ local vars RecurringTask class shares with Task class
#   - [1a] So, to reduce redundancy & maintain effeciency, RecurringTask passes on 




