def task():
    tasks=[] #an empty list
    print("Welcome To the Task Management App!!")
    total_tasks=int(input("Enter how many tasks u want to add"))
    for i in range(1,total_tasks+1):
        task_name=input(f"Enter task {i} :")
        task.append(task_name)
    print(f"Today's tasks are {tasks}")   
    while True:
       operation=int(input("Enter 1 : Add \n 2 : Update \n 3 : Delete \n 4 : View \n 5 : Exit"))
       if operation==1:
           Add=input("Enter task to add")
           tasks.append(Add)
           print(f"Task {Add} has been added...")

       elif operation==2:
           update=input("Enter the task u want to update:")  
           if update in tasks:
               up=input("Enter new task")
               ind=tasks.index(update)
               tasks[ind]=up
               print(f"Updated {update} to {up}")

       elif operation==3:
                  delete=input("Which task u want to delete?")
                  if delete in tasks:
                       ind=tasks.index(delete)
                       del tasks[ind]
                       print(f"Task {delete} has been deleted")

       elif operation==4:
            print(f"Total Tasks : {tasks}") 


       elif operation==5:
            print("Closing the program")
            break    
       else:
            print("Invalid input")       