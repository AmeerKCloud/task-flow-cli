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
            frequency_display = "daily"                   #⬅️[2] 'self.frequency' mutation bug fixed by adding 'frequency_display'.  See notes.
        elif self.frequency == "w":
            frequency_display = "weekly"
        else:
            frequency_display = "unknown"

        return f"{description_from_task} Frequency: {frequency_display}"    #⬅️[2a]

# NOTE:
#[1]-[1b] To demonstrate class inheritance.
#   - [1] Parameters/local vars that RecurringTask class shares with Task class.
#   - [1a] So, to reduce redundancy & maintain effeciency, RecurringTask passes on the 
#          shared params/vars & their values to Task class by calling the superclass' 
#          __init__ method, where said values get turned into attributes which the 
#          inheriting class (RecurringTask) then inherits via the 'super.__init__()' call.
#   - [1b] 'frequency' is the only param/var that RecurringTask does not share with Task. 
#          Therefor, it has to create a local attribute to store the value.

#[2] - Bug fixed: Initially, before adding local variable 'frequency_display', i was:
# - mutating 'self.frequency' by reassigning it 'daily' from 'd' or 'weekly' from 'w'.
#     > This caused a bug where when i tried to access the description of any recurring_task 
#     object, it would return 'None' after the initial creation.
#     > This is because 'self.frequency' would fail to match any of the conditions in the 
#         if-elif-else statement as its value had mutated.
#     > IMPORTANT: a method called 'describe()' should NOT  be mutating data if it's only 
#         purpose is to return a description.
# - Solution: Adding a local variable 'frequency_display' which is assigned and shows 
#   'weekly' or 'daily' instead of overwriting self.frequency.
#   > Now self.frequency stays "d" or "w" permanently (the actual stored data), while 
#     frequency_display is just a temporary, readable version used only for this one 
#     printout — calling describe() any number of times will always work correctly.


