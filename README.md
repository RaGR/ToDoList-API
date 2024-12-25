Dementalization for the project:

## Project Structure
```
To Do List App/
│
├── __init__.py
├── app.py
├── domain/
│   ├── __init__.py
│   ├── todo_item.py
│   └── todo_list.py
├── infrastructure/
│   ├── __init__.py
│   ├── in_memory_todo_repository.py
│   └── terminal_todo_presenter.py
├── interface/
│   ├── __init__.py
│   └── todo_service_interface.py
├── main.py
└── utils/
    ├── __init__.py
    └── helpers.py
```


## Basic Algorithm of the Program

1. **Add New Task**
   - Get input
   - Put to database
   - **Setup SQLite system!!!**
   
2. **Delete Task**
   - Select task to delete
   
3. **Update Task**
   - Show task title
   - Select task
   - Show detail
   - Get new input
   - Save to database
   
4. **Exit App**
   - How to halt in Python code?
