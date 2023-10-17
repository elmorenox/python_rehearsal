import psutil as ps
import os
import csv

# name our csv file
csv_file = "processes_info.csv"

# create a list to store dictionaries with process info
processes = []

# iterate through all processes with a provided iterator function
# this is recommended over looping over a list of all processes
# because iterating over a list may result in trying to access a process which has terminated
for proc in ps.process_iter():
    # get process info as a dictionary with the provided as_dict method
    pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'memory_info', 'cpu_percent'])
    # override cpu percent value to store the current cpu percent at a given time
    pinfo['cpu_percent'] = proc.cpu_percent(interval=0.1)
    # override memory info value to store the current memory usage at a given time
    pinfo['memory'] = pinfo['memory_info'].rss
    processes.append(pinfo)


# pass the processes list to the csv writer using dictionary writer
with open(csv_file, 'w', newline='') as file:
    # fieldnames is a list of the keys in the dictionary. ignore extra keys
    writer = csv.DictWriter(file, fieldnames=["pid", "name", "exe", "memory", "cpu_percent"], extrasaction='ignore')
    writer.writeheader()
    writer.writerows(processes)
