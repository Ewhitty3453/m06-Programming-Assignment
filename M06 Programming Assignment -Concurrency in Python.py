#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime

# 13.1 
current_date_string = datetime.datetime.now().strftime("%Y-%m-%d")
with open("today.txt", "w") as file:
    file.write(current_date_string)


# In[ ]:


# 13.2 
with open("today.txt", "r") as file:
    today_string = file.read()


# In[ ]:


# 13.3
parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d")
print(parsed_date)


# In[ ]:


import multiprocessing
import random
import time
import datetime

def worker():
    # Generate a random number of seconds between 0 and 1
    wait_time = random.random()
    # Wait for the random time
    time.sleep(wait_time)
    # Print the current time
    print(f"Process {multiprocessing.current_process().name} - Current Time: {datetime.datetime.now()}")
    # Exit the process
    exit()

if __name__ == "__main__":
    # Create three separate processes
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=worker, name=f"Worker-{i+1}")
        processes.append(process)
        process.start()

    # Join all processes
    for process in processes:
        process.join()

