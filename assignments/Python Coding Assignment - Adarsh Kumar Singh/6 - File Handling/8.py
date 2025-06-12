import datetime

def log_message(message, filename="logfile.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(filename, "a") as file:
        file.write(log_entry)

log_message("Program started")
log_message("Performing task")
log_message("Program finished")
