todo_list=[]
task=""
user_mark=''
marked=[]#write function to create a task

def create_task(task):
    task= input("Enter task: ")
    todo_list.append(task)
    print(todo_list)


def delete_task(task):
    for task in todo_list:
        todo_list.remove(task)
    print (todo_list)

def mark_as_finished(task):
    user_choice=input("Choose task to mark:")
    marked.append(user_choice)
    for i in marked:
        if i == user_choice:
            
            print(True)
            print("These are finished:{}".format(marked))
        else:
            print (False)
            print("Please enter valid task")


def delete_all_tasks():
    todo_list.clear()
    print("No tasks")
    
