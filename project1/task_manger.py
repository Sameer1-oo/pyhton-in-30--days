def task():
    tasks=[]
    print("--welcome to task manger--")
    total_task=int(input("how many task you do in the day "))
    for i in range(1,total_task+1):
        taskname=input("enter the today task {i} =")
        tasks.append(taskname)
        print("\n Today's tasks are : ")
        for t in tasks :
            print(f"{t}")
