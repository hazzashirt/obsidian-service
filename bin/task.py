#%% Task
from datetime import datetime as dt
class task:

    def __init__(self, text, date=None, priority=None, time=None, id=None, tags=None):
        if priority: self.priority=priority
        else: self.priority = 3
        if date: self.date = date
        else: self.date = dt.today().date()
        if time: self.time = time
        else: self.time = dt.now().time()
        if id: self.id = id
        else: self.id = -1
        if tags: self.tags = tags
        else: self.extractTags()
        self.text = text

    def toString(self):
        return ("%s, due: %s %s" % (self.text,self.date, self.time))
    
    def extractTags(self):
        self.tags = []
        for word in self.text:
            if word in tagList:
                self.tags.append(word)
        

# item = task("do the thing")
# text = item.toString()
# print(text)

class schedule:
    def __init__(self, taskList=None):
        if taskList:
            for task in taskList:
                self.items.append(task)
        else: self.items = []

    def reschedule(self, task_id):
        print("incomplete method")

    def schedule(self, task_id):
        print("find earliest timeslot")