import shutil
import os
import logging

def check_disk_usage(path="/", threshold=80):
    usage = shutil.disk_usage(path)
    percent_used = (usage.used / usage.total) * 100
    if percent_used > threshold:
        logging.warning(f"DISK ALERT: {path} is {percent_used:.2f}% full!")
        return True
    logging.info(f"Disk usage for {path}: {percent_used:.2f}%")
    return False

if __name__ == "__main__":
    check_disk_usage()
