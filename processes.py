import psutil as ps
import os
import csv

csv_file = "processes_info.csv"
processes = []
for proc in ps.process_iter():
    pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'memory_info', 'cpu_percent'])
    pinfo['cpu_percent'] = proc.cpu_percent(interval=0.1)
    pinfo['memory'] = pinfo['memory_info'].rss
    processes.append(pinfo)


with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["pid", "name", "exe", "cpu_percent", "memory"], extrasaction='ignore')
    writer.writeheader()
    writer.writerows(processes)