class Task: 
    def __init__(self, title, status="ToDo"): 
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repre__(self): 
        return f"{self.title} = {'Done' if self.completed else 'ToDo'}"

    def __str__(self): 
        return f"Task: {self.title}, Status: {self.status}"
