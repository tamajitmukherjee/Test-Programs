#Task Manager Program to let a user add, view, edit and delete tasks or exit
#A task will contain task title and description only

tasks = []
taskId = 0
taskTitle, taskDetail
def addTask():
	taskTitle = input("Enter Task Title: ")
	taskDetail = input("Enter Task Detail: ")
	global taskId
	taskId += 1
	tasks.append({"taskID":taskID, "taskTitle":taskTitle, "taskDetail":taskDetail})
	print ("Task added successfully!")

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
	print ("All the active tasks are as follows: ")
	for taskCount in range(len(tasks)-1):
    		print(tasks[taskCount])

def deleteTask():
	viewTask()
	deleteTaskID= int(input("Enter the task number you want to delete: "))
	del task [(taskID-1)]

while True:
	print("Welcome to Tamajit's task manager application built specially for you!")
	print("Please select the task number which you want to perform: ")
	print(	" 1. Add a task" )
	print(	" 2. Edit a task")
	print(	" 3. View a task")
	print(	" 4. Delete a task")
	print(	" 5. Exit")
	taskOption = int(input("Enter the task number: ")) - 1
	if taskOption == 0:
		addTask()
	elif taskOption == 1:
		editTask()
	elif taskOption == 2:
		viewTask()
	elif taskOption == 3:
		deleteTask()
	elif taskOption == 4:
		break
	else:
		continue
	

	
	
	
