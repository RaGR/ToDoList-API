import sys

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

print("To Do List APP")
print("-------------------------")
print("1. add new task") #-> get input -> put to database ==> setup SQlite sys!!!
print("2. delete task") #-> select task to delete
print("3. update task") #-> show task title -> select task -> show detail -> get new input -> save to database
print("5. exit app") #-> how to halt in py code

usr_input = input("please enter your task: ")

if usr_input == "5": exit_program()

elif usr_input == "1":

elif usr_input == "2":

elif usr_input == "3":
    
elif usr_input == "4":

