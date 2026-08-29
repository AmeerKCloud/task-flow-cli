# This module demonstrates the use of the following python concepts: 
# Classes, Objects, Attributes, Methods, Object State & Instances

# Here, all of the main task classes will exist.

class Task:
    count = 0     #⬅️ # class attribute — one shared value between all objects, exists before any object is made. Tracks how many Task objects have been created.

    def __init__(self, title, priority = "medium", done = False):
        self.title = title
        self.priority = priority
        self.done = done
        Task.count += 1     #⬅️ Updates the shared class attribute.

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
        description_from_task = super().describe()

        if self.frequency == "d":
            self.frequency = "daily"
            print(f"{description_from_task} Frequency: {self.frequency}")
        elif self.frequency == "w":
            self.frequency = "weekly"
            print(f"{description_from_task} Frequency: {self.frequency}")

# NOTE:
#[1]-[1b] To demonstrate class inheritance.
#   - [1] Parameters/local vars that RecurringTask class shares with Task class.
#   - [1a] So, to reduce redundancy & maintain effeciency, RecurringTask passes on the 
#          shared params/vars & their values to Task class by calling the superclass' 
#          __init__ method, where said values get turned into attributes which the 
#          inheriting class (RecurringTask) then inherits via the 'super.__init__()' call.
#   - [1b] 'frequency' is the only param/var that RecurringTask does not share with Task. 
#          Therefor, it has to create a local attribute to store the value.




