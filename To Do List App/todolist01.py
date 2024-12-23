import sys
import sqlite3

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

def create_table():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY, task TEXT)''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    print(f"Task '{task}' added successfully! ✅")

def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print(f"Task with ID '{task_id}' deleted successfully! ✅")

def update_task(task_id, new_task):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
    conn.commit()
    conn.close()
    print(f"Task with ID '{task_id}' updated successfully! ✅")

def list_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        print("Current tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}")
    else:
        print("No tasks found! 📭")

create_table()

while True:
    print("\nTo Do List APP")
    print("-------------------------")
    print("1. Add new task")    #Create
    print("2. List tasks")      #Read
    print("3. Update task")     #Update
    print("4. Delete task")     #Dellete
    print("5. Exit app")

    usr_input = input("Please enter your option (1-5): ")

    if usr_input == "5":
        exit_program()
    elif usr_input == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif usr_input == "2":
        list_tasks()
    elif usr_input == "3":
        list_tasks()
        task_id = int(input("Enter the ID of the task to update: "))
        new_task = input("Enter the new task: ")
        update_task(task_id, new_task)
    elif usr_input == "4":
        list_tasks()
        task_id = int(input("Enter the ID of the task to delete: "))
        delete_task(task_id)
    else:
        print("Invalid option! Please choose a number between 1 and 5. ❌")
