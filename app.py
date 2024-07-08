import time
from datetime import datetime
import schedule


def log_message():
    message = f"Script ran at {datetime.now()}\n"
    with open("log.txt", "w") as file:
        file.write(message)
    print(message)


def stop_running():
    global keep_running
    keep_running = False
    print("Stopping the scheduler.")


schedule.every(10).seconds.do(log_message)
schedule.every(1).minute.do(stop_running)

keep_running = True

while keep_running:
    schedule.run_pending()
    time.sleep(2)

print("program finished")