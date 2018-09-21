from tasks import todo_list,create_task,delete_task,delete_all_tasks,mark_as_finished
from accounts import accounts, add_account,login,user


if __name__ =='__main__':


    name=input("Enter your name:  ")
    password=''
    
    while name in accounts:
        login(name,password)   
        print("{} you are logged in".format(name))     
     
    else:

        add_account(name,password)

    print ("{} now you can proceed to your to-do list".format(name))

    print ("Select Option")
    print(20 * "-", "MENU", 20 * "-")
    print("0.Login")
    print("1. creating a task")
    print("2. deleting a task")
    print("3. Marking a task as task as finished")
    print("4. deleting all tasks")
    print("5. Logout")



    loop = True #this keeps app running until it meets false
    task=''    
    while loop:
        selection = int(input("selection: "))

        if selection== 1:
            print("1.Creating a task")
            create_task(task)
            print(todo_list)
        elif selection ==2 :
            print("2.Deleting a task")
            task=str(input("Enter task you want to delete: "))
            print(todo_list)
            delete_task(task)
        elif selection ==3:
            print("3. Marking a task as finished")
            print(todo_list)
            task=str(input("Enter task you want to mark: "))
            mark_as_finished(task)
        elif selection==4:
            print("3.Deleting all tasks")
            print(todo_list)
            delete_all_tasks(task)
            print(todo_list)
        elif selection ==5:
            print("5. You are leaving application")
            loop=False #this will set the loop to close, hence end program
        else:
            print("Selection doesnot exist. Enter a valid selection ")  #when one enters a number out of the menu range


    

       