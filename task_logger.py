import os
from datetime import datetime

file = datetime.now().strftime('%B %Y') + ".txt"
#Note: Directory will need to be changed
file_location = "FILE_LOCATION_HERE" + file

if os.path.exists(file_location):
    pass
else:
    #this creates new logging file
    new = open(file_location, "w")
    n_log = "This is meant to be a log to help keep track of tasks done for the day. A new file is created when the\nmonth changes. Entries are written informally to make it easy to immediately\nlog new events."
    new.writelines(n_log)
    new.close()

logfile = file_location

with open(logfile, "r") as f:
    logged = f.read()
    current = datetime.now().strftime('%B %d, %Y')
    if current in logged:
        existing = True
    else:
        existing = False
if existing == True:
    with open(logfile, "a") as f:
        while True:
            log = input("Additional entry today: ")
            f.write(log)
            f.write("\n")
            ask = input("Are you done? (Y/N): ")
            if ask.upper() == 'Y':
                break
            else:
                continue
else:
    with open (logfile, "a") as f:
        formatted = "\n \n[{}]\n \n".format(current)
        f.write(formatted)
        while True:
            log = input("Entry: ")
            f.write(log)
            f.write("\n")
            ask = input("Are you done? (Y/N) ")
            if ask.upper() == 'Y':
                break
            else:
                continue
