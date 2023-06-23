import time

def focus_clock(duration):
    start_time = time.time()
    end_time = start_time + duration * 60 # convert duration from minutes to seconds
    
    while time.time() < end_time:
        remaining_time = round(end_time - time.time())
        print(f"Remaining time: {remaining_time} seconds")
        time.sleep(1)
    
    print("Time's up! Take a break.")

# Example usage:
focus_clock(25) # runs a 25-minute focus session
