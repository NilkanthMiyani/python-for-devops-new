import psutil
import shutil

# Get thresholds from user
cpu_threshold = int(input("Enter CPU threshold: "))
disk_threshold = int(input("Enter Disk threshold: "))
memory_threshold = int(input("Enter Memory threshold: "))

# Get system metrics
cpu = psutil.cpu_percent(interval=1)
disk = (shutil.disk_usage('C:/').used / shutil.disk_usage('C:/').total) * 100
memory = psutil.virtual_memory().percent

# Check and print results
if cpu > cpu_threshold:
    print("Alert: CPU usage is high")
else:
    print("CPU usage is normal")

if disk > disk_threshold:
    print("Alert: Disk usage is high")
else:
    print("Disk usage is normal")

if memory > memory_threshold:
    print("Alert: Memory usage is high")
else:
    print("Memory usage is normal")
