tasks = []
taskId = 0  # Global task ID

def addTask():
    global taskId
    taskId += 1  # Increment the global task ID
    taskTitle = input("Enter Task Title: ")
    taskDetail = input("Enter Task Detail: ")
    tasks.append({"taskID": taskId, "taskTitle": taskTitle, "taskDetail": taskDetail})
    print("Task added successfully!")

def editTask():
    viewTask()
    editTaskID = int(input("Enter the task ID you want to edit: ")) - 1
    if 0 <= editTaskID < len(tasks):
        tasks[editTaskID]["taskTitle"] = input("Enter New Task Title: ")
        tasks[editTaskID]["taskDetail"] = input("Enter New Task Detail: ")
        print("Task updated successfully!")
    else:
        print("Invalid Task ID!")

def viewTask():
    if not tasks:
        print("No tasks available.")
        return
    print("All the active tasks are as follows: ")
    for task in tasks:
        print(f"Task ID: {task['taskID']}, Title: {task['taskTitle']}, Detail: {task['taskDetail']}")

def deleteTask():
    viewTask()
    deleteTaskID = int(input("Enter the task ID you want to delete: ")) - 1
    if 0 <= deleteTaskID < len(tasks):
        del tasks[deleteTaskID]
        print("Task deleted successfully!")
    else:
        print("Invalid Task ID!")

while True:
    print("Welcome to Tamajit's task manager application built specially for you!")
    print("Please select the task number which you want to perform: ")
    print(" 1. Add a task")
    print(" 2. Edit a task")
    print(" 3. View tasks")
    print(" 4. Delete a task")
    print(" 5. Exit")
    taskOption = int(input("Enter the task number: "))
    if taskOption == 1:
        addTask()
    elif taskOption == 2:
        editTask()
    elif taskOption == 3:
        viewTask()
    elif taskOption == 4:
        deleteTask()
    elif taskOption == 5:
        break
    else:
        print("Invalid option. Please try again.")
