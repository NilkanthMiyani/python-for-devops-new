# Take CPU threshold from user
# Find the correct cpu usage
# if CPU usage is greater than threshold then email the use

import psutil # import the lib fom pypi

def get_cpu_threshold():
    user_cpu = int(input("Enter the CPU threshold: "))

    currunt_cpu = psutil.cpu_percent(interval=1)

    if currunt_cpu >= user_cpu:
        print("CPU usage is high, sending email to user...")

    else:
        print("CPU usage is normal")

get_cpu_threshold()