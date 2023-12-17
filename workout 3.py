# run timing 

def run_timing():
    total_run_time = 0
    count = 0

    while True:
        run_time = input("Enter 10km runtime:")
        if not run_time:
            break
        total_run_time+=float(run_time)
        count+=1

    average_run_time = total_run_time/count

    print(f'\nAverage of {average_run_time}, over {count} runs')
    return average_run_time


run_timing()