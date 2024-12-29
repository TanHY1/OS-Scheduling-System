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
    print("Completion Times:", completed)

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
    print("SJN Completion Times:", completed)

if __name__ == '__main__':
    while True:
        print("Welcome to the CPU Scheduling Algorithm Simulator!")
        print("Please choose a scheduling algorithm:")
        print("1. Round Robin")
        print("2. Shortest Job Next (SJN)")
        print("3. Preemptive Priority")
        print("4. Non-preeemptive Priority")
        print("Please enter the number of the algorithm you want to use:")
        choice = int(input())
        if 1 <= choice <= 4:
            if choice == 1:
                print("You choose Round Robin")
                print()
                while True:
                    print("Please enter how many processes you want to schedule (1-10):")
                    num_processes = int(input())
                    if num_processes < 1 or num_processes > 10:
                        print("Invalid number of processes. Please enter a number between 1 and 10.")
                    else:
                        break
                    
                print("Please enter the time quantum:")
                time_quantum = int(input())
                
                RoundRobin_process_list = []
                for i in range(num_processes):
                    process_id = input(f"Please enter the process ID for process {i+1}: ")
                    while True:
                        arrival_time = int(input(f"Please enter the arrival time for process {process_id}: "))
                        burst_time = int(input(f"Please enter the burst time for process {process_id}: "))
                        if (burst_time < 0 or arrival_time < 0):
                            print("Invalid burst time or arrival time. Please enter a positive number.")
                        else: 
                            RoundRobin_process_list.append([process_id, arrival_time, burst_time])
                            break
                    print()
                
                print("Process list:", RoundRobin_process_list)

                #process_list = [["P1", 0, 10], ["P2", 1, 2], ["P3", 2, 3], ["P4", 3, 1], ["P5", 4, 5]]
                round_robin(RoundRobin_process_list, time_quantum)
                break

            #Shortest Job Next (SJN)
            elif choice == 2:
                print("You have chosen Shortest Job Next (SJN).")
                print("Please enter how many processes that you want to schedule:")
                while True:
                    num_processes = int(input())
                    if num_processes < 0:
                        print("Invalid number of processes. Please enter a positive number.")
                    else:
                        break
                
                SJN_process_list = []

                for i in range(num_processes):
                    process_id = input(f"Please enter the process ID for process {i+1}: ")
                    while True:
                        arrival_time = int(input(f"Please enter the arrival time for process {process_id}: "))
                        burst_time = int(input(f"Please enter the burst time for process {process_id}: "))
                        priority = int(input(f"Please enter the priority for process {process_id}: "))
                        if (burst_time < 0 or arrival_time < 0 or priority < 0):
                            print("Invalid burst time, arrival time or priority. Please enter a positive number.")
                        else:
                            SJN_process_list.append([process_id, arrival_time, burst_time, priority])
                            break
                    print()
                print("Shortest Job Next (SJN) process list:", SJN_process_list)

                shortest_job_next(SJN_process_list)
                break
            
            elif choice == 3:
                print("You have chosen Preemptive Priority.")
                print("Please enter how many processes that you want to schedule:")
                while True:
                    num_processes = int(input())
                    if num_processes < 0:
                        print("Invalid number of processes. Please enter a positive number.")
                    else:
                        break
                
                PreemptivePriority_process_list = []

                for i in range(num_processes):
                    process_id = input(f"Please enter the process ID for process {i+1}: ")
                    while True:
                        arrival_time = int(input(f"Please enter the arrival time for process {process_id}: "))
                        burst_time = int(input(f"Please enter the burst time for process {process_id}: "))
                        priority = int(input(f"Please enter the priority for process {process_id}: "))
                        if (burst_time < 0 or arrival_time < 0 or priority < 0):
                            print("Invalid burst time, arrival time or priority. Please enter a positive number.")
                        else:
                            PreemptivePriority_process_list.append([process_id, arrival_time, burst_time, priority])
                            break
                    print()
                print("Preemptive Priority process list:", PreemptivePriority_process_list)

                #preemptive_priority(PreemptivePriority_process_list)
                break
            elif choice == 4:
                print("You have chosen Non-preeemptive Priority.")
                print("Please enter how many processes that you want to schedule:")
                while True:
                    num_processes = int(input())
                    if num_processes < 0:
                        print("Invalid number of processes. Please enter a positive number.")
                    else:
                        break
                
                NonPreemptivePriority_process_list = []

                for i in range(num_processes):
                    process_id = input(f"Please enter the process ID for process {i+1}: ")
                    while True:
                        arrival_time = int(input(f"Please enter the arrival time for process {process_id}: "))
                        burst_time = int(input(f"Please enter the burst time for process {process_id}: "))
                        priority = int(input(f"Please enter the priority for process {process_id}: "))
                        if (burst_time < 0 or arrival_time < 0 or priority < 0):
                            print("Invalid burst time, arrival time or priority. Please enter a positive number.")
                        else:
                            NonPreemptivePriority_process_list.append([process_id, arrival_time, burst_time, priority])
                            break
                    print()
                print("Non-preemptive Priority process list:", NonPreemptivePriority_process_list)

                #non_preemptive_priority(NonPreemptivePriority_process_list)
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



    '''
    process_list = [["P1", 0, 10], ["P2", 1, 2], ["P3", 2, 3], ["P4", 3, 1], ["P5", 4, 5]]
    time_quantum = 3
    round_robin(process_list, time_quantum)
    '''
    

