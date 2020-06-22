import csv
from datetime import datetime
import logging
import os

list_of_csv = [["name1.csv"], ["name2.csv"], ["name3.csv"], ["name4.csv"], ["name5.csv"]]
today = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
log_time = datetime.today().strftime("%H:%M:%S")

file_name = "Tasks/Lesson6/" + today + "_flat_file.csv"
log_file = "Tasks/Lesson6/Log.txt"
log = open(log_file, "w")

try:
    with open(file_name, "w", newline="") as file:
        write_file = csv.writer(file)
        

        for i in list_of_csv:
            write_file.writerow(i)
            log.write(log_time + " copy file " + str(i) + " to " + str(file_name) + "\n")

        log.close()
        file.close()
        
        #delete log file
        os.remove(log_file)
except:
    log.write(log_time + " unable to open a file\n")