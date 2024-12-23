Dementalization for the project:

Project structure:
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

Basic algorithm of the program:
1. add new task	-> get input -> put to database ==> setup SQlite sys!!!
2. delete task	 -> select task to delete
3. update task	-> show task title -> select task -> show detail -> get new input -> save to database
5. exit app 	-> how to halt in py code
