def non_preemptive_priority(non_PreemptivePriority_process_list):
    # testing
    print("Non-Preemptive Priority process list:", non_PreemptivePriority_process_list)

    time = 0
    non_PreemptivePriority_gantt_chart = []
    completed = {}
    non_PreemptivePriority_waiting_queue = []

    # Sort process list by arrival time
    non_PreemptivePriority_process_list.sort(key=lambda x: x[1])

    # Keep track of processes that have been started but not yet completed
    remaining_burst = {p[0]: p[2] for p in non_PreemptivePriority_process_list}

    while non_PreemptivePriority_process_list or non_PreemptivePriority_waiting_queue:
        # Add any arrived processes to the waiting queue
        # eg: Pid, arrival time, burst time, priority = Pid, Arrival time
        while non_PreemptivePriority_process_list and (non_PreemptivePriority_process_list[0][1] <= time):
            # Pop the first process from the process list into the waiting queue
            non_PreemptivePriority_waiting_queue.append(non_PreemptivePriority_process_list.pop(0))

        # If there are processes in the waiting queue, choose the process with the highest priority
        # x[3] = priority
        if non_PreemptivePriority_waiting_queue:
            non_PreemptivePriority_waiting_queue.sort(key=lambda x: x[3], reverse=False)
            process = non_PreemptivePriority_waiting_queue.pop(0)
            non_PreemptivePriority_gantt_chart.append(process[0])

            # Execute the process until it finish
            time += remaining_burst[process[0]]
            completed[process[0]] = time

        else:
            non_PreemptivePriority_gantt_chart.append("Idle")
            time += 1

    print("Non-Preemptive Priority Gantt Chart:", non_PreemptivePriority_gantt_chart)
    print()
    print("Non-Preemptive Priority Completed:", completed)
    return completed