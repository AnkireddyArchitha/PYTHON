from  collections  import deque
def Find(tasks,time_slice):
    Q=deque()
    for i in range(len(tasks)):
        Q.append((tasks[i],i+1))
    time=0
    while Q:
        task,task_num=Q.popleft()
        executed=min(task,time_slice)
        time=time+executed
        print("task {} -> executed {} units :time {}".format(task_num,executed,time))
        if(task)>time_slice:
            Q.append((task-executed,task_num))
tasks=[10,5,8]
time_slice=4
Find(tasks,time_slice)
