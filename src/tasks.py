todo_list=[]


def create_task_id():
    return len(todo_list)+1

def create_task(task):
    task= str(input("Enter task: "))
    a_task=dict()
    detailed= input("Enter task details: ")
    if task not in todo_list:
        a_task['title']=task
        a_task['detailed']=detailed
        a_task['id']=create_task_id()

        return todo_list.append(a_task)
    


def delete_task(task):
 
    for item in range(len(todo_list)):
        if todo_list[item]['title'] ==task:
            del todo_list[item]
            print ("You have deleted {}".format(task))
        
            print("These are remaining  {}".format(len(todo_list)))
        # print("Task not in current list")
        
        

def mark_as_finished(task):
    
    for item in todo_list:
        if item['title'] == task:
            item['title']= task+("[Finished]")
            print("These are finished:{}".format(item))
        # print("Task not in current list")


def delete_all_tasks(task):
    todo_list.clear()
    print("You have deleted all tasks")
    
