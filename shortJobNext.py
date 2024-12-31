def shortest_job_next(SJN_process_list):
    # Shortest Job Next = [process_id, arrival_time, burst_time]
    time = 0
    SJN_gantt_chart = []
    completed = {}
    SJN_waiting_queue = []

    # Sort process list by arrival time
    SJN_process_list.sort(key=lambda x: x[1])

    # Keep track of processes that have been started but not yet completed
    # p[0] = process_id, p[2] = burst time
    SJN_burst_time = {p[0]: p[2] for p in SJN_process_list}

    while SJN_process_list or SJN_waiting_queue:
        # Add any arrived processes to the waiting queue
        while SJN_process_list and (SJN_process_list[0][1] <= time):
            SJN_waiting_queue.append(SJN_process_list.pop(0))

        # If there are processes in the waiting queue, choose the process with the shortest burst time
        if SJN_waiting_queue:
            SJN_waiting_queue.sort(key=lambda x: x[2])
            process = SJN_waiting_queue.pop(0)
            SJN_gantt_chart.append(process[0])

            # Execute the process until it finishes
            time += SJN_burst_time[process[0]]
            completed[process[0]] = time

        else:
            SJN_gantt_chart.append("Idle")
            time += 1

    print("SJN Gantt Chart:", SJN_gantt_chart)
    print()
    print("SJN Completion Times:", completed)