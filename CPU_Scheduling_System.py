from roundRobin import round_robin
from shortJobNext import shortest_job_next

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
                print(round_robin(RoundRobin_process_list, time_quantum))

                #process_list = [["P1", 0, 10], ["P2", 1, 2], ["P3", 2, 3], ["P4", 3, 1], ["P5", 4, 5]]
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


