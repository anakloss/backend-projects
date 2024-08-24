# Task Tracker CLI
Task Tracker CLI is a simple command-line application that allows you to add, update and delete tasks. Also lets you change status and list of tasks based on their status.
Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## How to run
Clone the repository and run the following command:
```
git clone https://github.com/anakloss/backend-projects.git
cd backend-projects/task-tracker
```
Run the following command to build and run the project:
```
# To see the list of available commands
py .\tasks.py --help

# To add a task
py .\tasks.py add "Buy fruits"

# To update a task
py .\tasks.py update 1 "Buy fruits and vegetables"

# To delete a task
py .\tasks.py delete 1

# To mark a task as in progress/done
py .\tasks.py mark-in-progress 1
py .\tasks.py mark-done 1

# To list all tasks
py .\tasks.py list or py .\tasks.py list all
py .\tasks.py list done
py .\tasks.py list todo
py .\tasks.py list in-progress
```

## Notes
* Ensure that the test tasks.json file exists in the same directory as the script for it to function correctly.
* The application will create the tasks.json file if it does not already exist when adding a new task.