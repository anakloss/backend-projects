import json
import os
import argparse
from datetime import datetime


# Archivo json donde se almacenan las tareas
TASKS_FILE = 'tasks.json'

# Get tasks from a JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Set tasks into a JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Insert new task into a JSON file
def add_task(description):
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: {description}')

# Update description from a task based on 'ID'
def update_task_description(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Update task {task_id}: {new_description}.')
            return
    print(f'Task {task_id} not found.')

# Change task status based on 'ID'
def update_task_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {new_status}.')
            return
    print(f'Task {task_id} not found.')

# Delete a task based on 'ID'
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(new_tasks):
        print(f'Task {task_id} not found.')
        return
    save_tasks(new_tasks)
    print(f'Task {task_id} deleted.')

# List all tasks or filter by status
def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print('No tasks available.')
        return
    
    filtered_tasks = tasks
    if filter_status:
        filtered_tasks = [task for task in tasks if task['status'] == filter_status]

    if not filtered_tasks:
        print('No matching tasks found.')
        return
    
    for task in filtered_tasks:
        print(f"{task['id']}: {task['description']} [{task['status']}] (Created: {task['createdAt']}, Updated: {task['updatedAt']})")

def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for adding a task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # Subparser for listing tasks
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', type=str, nargs='?', choices=['all', 'done', 'todo', 'in-progress'], default='all', help='Filter tasks by status')

    # Subparser for marking a task as complete
    complete_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    complete_parser.add_argument('id', type=int, help='ID of the task to complete')

    # Subparser for marking a task as in-progress
    in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in-progress')
    in_progress_parser.add_argument('id', type=int, help='ID of the task to mark as in-progress')

    # Subparser for updating a task
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description of the task to update')
    
    # Subparser for deleting a task
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        if args.status == 'all':
            list_tasks()
        else:
            list_tasks(args.status)
    elif args.command == 'mark-done':
        update_task_status(args.id, 'done')
    elif args.command == 'mark-in-progress':
        update_task_status(args.id, 'in-progress')
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'update':
        update_task_description(args.id, args.description)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()