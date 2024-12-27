#input: process list, time quantum
#process_list format: [pid, arrival time, burst time]

def round_robin(process_list, time_quantum):
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
                
                process_list = []
                for i in range(num_processes):
                    process_id = input(f"Please enter the process ID for process {i+1}: ")
                    arrival_time = int(input(f"Please enter the arrival time for process {process_id}: "))
                    burst_time = int(input(f"Please enter the burst time for process {process_id}: "))
                    process_list.append([process_id, arrival_time, burst_time])
                    print()
                
                print("Process list:", process_list)


                #process_list = [["P1", 0, 10], ["P2", 1, 2], ["P3", 2, 3], ["P4", 3, 1], ["P5", 4, 5]]
                round_robin(process_list, time_quantum)
                break
            elif choice == 2:
                print("You have chosen Shortest Job Next (SJN).")
                break
            elif choice == 3:
                print("You have chosen Preemptive Priority.")
                break
            elif choice == 4:
                print("You have chosen Non-preeemptive Priority.")
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



    '''
    process_list = [["P1", 0, 10], ["P2", 1, 2], ["P3", 2, 3], ["P4", 3, 1], ["P5", 4, 5]]
    time_quantum = 3
    round_robin(process_list, time_quantum)
    '''
    

