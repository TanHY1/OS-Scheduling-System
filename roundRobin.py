def round_robin(process_list, time_quantum):
    #round_robin: [pid, arrival time, burst time]
    time = 0
    gantt_chart = []
    completed = {}
    waiting_queue = []

    # Sort the process list by arrival time
    process_list.sort(key=lambda x: x[1])

    # Keep track of processes that have been started but not yet completed
    remaining_burst = {p[0]: p[2] for p in process_list}

    while process_list or waiting_queue:
        # Add any arrived processes to the waiting queue
        while process_list and process_list[0][1] <= time:
            waiting_queue.append(process_list.pop(0))

        if waiting_queue:
            process = waiting_queue.pop(0)
            gantt_chart.append(process[0])

            # Execute the process for the time quantum or remaining burst time
            if remaining_burst[process[0]] <= time_quantum:
                time += remaining_burst[process[0]]
                completed[process[0]] = time
                remaining_burst[process[0]] = 0
            else:
                time += time_quantum
                remaining_burst[process[0]] -= time_quantum

                # Add any newly arrived processes to the waiting queue
                while process_list and process_list[0][1] <= time:
                    waiting_queue.append(process_list.pop(0))

                # Requeue the current process
                waiting_queue.append(process)
        else:
            gantt_chart.append("Idle")
            time += 1

    print("Gantt Chart:", gantt_chart)
    print()
    print("Completed Processes:", completed)
    return completed