from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Task(ABC):
    def __init__(self, task_id, task_name, deadline, priority="Low", status="Pending", color=""):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = deadline
        self.priority = priority
        self.status = status
        self.color = color

    @abstractmethod
    def color_your_task(self):
        pass

    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Deadline: {self.deadline}, Priority: {self.priority}, Status: {self.status}, Color: {self.color}"

class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline, priority="Low", status="Pending"):
        super().__init__(task_id, task_name, deadline, priority, status)
        self.color = "Blue"

    def color_your_task(self):
        self.color = "Blue"


class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline, priority="High", status="Pending"):
        super().__init__(task_id, task_name, deadline, priority, status)
        self.color = "Red"

    def color_your_task(self):
        self.color = "Red"


class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)
        print(f"Task '{task.task_name}' added successfully!")

    def display_tasks(self):
        print("Task List:")
        for task in self.task_list:
            print(task)

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def set_task_status(self, task_id, status):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            print(f"Task ID {task_id} status updated to '{status}'!")

    def set_prioritization(self, task_id, priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = priority
            print(f"Task ID {task_id} priority updated to '{priority}'!")

    def set_new_date(self, task_id, deadline):
        task = self.get_task_by_id(task_id)
        if task:
            task.deadline = deadline
            print(f"Task ID {task_id} deadline updated to '{deadline}'!")

    def mark_status_completed(self, task_id):
        self.set_task_status(task_id, "Completed")

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        print(f"Task with ID {task_id} not found!")
        return None

class TaskTracking:
    def __init__(self, task_management):
        self.task_management = task_management

    def get_task_status(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            return task.status
        return None

    def get_task_deadline(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            return task.deadline
        return None

    def get_task_color(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            return task.color
        return None

    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        print(f"Task with ID {task_id} not found!")
        return None

if __name__ == "__main__":
    task_mgmt = TaskManagement()
    editor = TaskEditing(task_mgmt)
    tracker = TaskTracking(task_mgmt)

    # Create PersonalTask and WorkTask
    task1 = PersonalTask(1, "Go Shopping", datetime.today(), "Low")
    task2 = WorkTask(2, "Finish Project", datetime.today() + timedelta(days=2), "High")

    # Add tasks to management system
    task_mgmt.add_task(task1)
    task_mgmt.add_task(task2)

    # Display tasks
    task_mgmt.display_tasks()

    # Edit task
    editor.set_task_status(1, "In Progress")
    editor.set_prioritization(1, "Medium")
    editor.set_new_date(2, datetime.today() + timedelta(days=5))

    # Track task
    print(f"Task 1 Status: {tracker.get_task_status(1)}")
    print(f"Task 2 Deadline: {tracker.get_task_deadline(2)}")

    # Mark task as complete
    editor.mark_status_completed(1)

    # Display tasks again
    task_mgmt.display_tasks()
