def task():
    tasks=[]
    print("-----Wlelcome to task manager-----")
    total_task=int(input("Enter how many task u want to add"))
    for i in range(1,total_task+1):
        task_name=input("Enter task {i}=")
        tasks.append(task_name)
    print("Today's tasks are\n{tasks}")
    while True:
        operation=int(input("Enter 1-Add\n Enter 2-Update\n Enter 3-Delete\nEnter 4-View\n Enter 5-Exit/Stop"))
        if operation==1:
            add=input("Enter task u want to add :")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
        elif operation==2:
            updated_val=input("Enter the task name you want to update :")
            if updated_val in tasks:
                up=input("Enter the new task :")
                ind=tasks.index(updated_val)  
                tasks[ind]=up
                print("Updated task {up}")
        elif operation ==3:
            del_val=input("Which task do u want to delete :")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print("Task {del_val} has been deleted successfully")
        elif operation==4:
                print("Total tasks :{tasks}")     
        elif operation==5:
            print("Thank you...")
            break
        else:
            print("Invalid input")           