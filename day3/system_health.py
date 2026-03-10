import psutil
import shutil


def get_threshold(prompt):
    """Prompt user for a numeric threshold, retrying on invalid input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0 or value > 100:
                print("Please enter a value between 0 and 100.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_system_metrics():
    """Collect current CPU, disk, and memory usage percentages."""
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_info = shutil.disk_usage('C:/')
    disk_usage = (disk_info.used / disk_info.total) * 100
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, disk_usage, memory_usage


def check_health(metric_name, current_value, threshold):
    """Compare a metric against its threshold and print the result."""
    if current_value > threshold:
        print(f"Alert: {metric_name} usage is high ({current_value:.1f}% > {threshold}%)")
    else:
        print(f"{metric_name} usage is normal ({current_value:.1f}%)")


def system_health():
    # Get thresholds from user
    cpu_threshold = get_threshold("Enter CPU threshold: ")
    disk_threshold = get_threshold("Enter Disk threshold: ")
    memory_threshold = get_threshold("Enter Memory threshold: ")

    # Get system metrics — wrapped in try/except so the script doesn't crash
    # if psutil or shutil encounter an OS-level error (e.g. permission denied,
    # unavailable disk path, or missing system libraries).
    try:
        cpu_usage, disk_usage, memory_usage = get_system_metrics()
    except Exception as e:
        print(f"Error reading system metrics: {e}")
        return

    # Check and print results
    check_health("CPU", cpu_usage, cpu_threshold)
    check_health("Disk", disk_usage, disk_threshold)
    check_health("Memory", memory_usage, memory_threshold)


if __name__ == "__main__":
    system_health()
