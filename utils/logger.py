from datetime import datetime


def write_log(option):
    with open("outputs/log.txt", "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"Date & Time : {current_time}\n")
        file.write(f"Selected Option : {option}\n")
        file.write("-" * 40 + "\n")