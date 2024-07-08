import time
from datetime import datetime


def log_message():
    message = f"Script ran at {datetime.now()}\n"
    with open("log.txt", "w") as file:
        file.write(message)
    print(message)


while True:
    log_message()
    time.sleep(2)