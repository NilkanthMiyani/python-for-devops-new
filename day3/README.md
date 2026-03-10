# Day 3 — System Health Monitor (Improved)

A Python script that monitors **CPU**, **Disk**, and **Memory** usage on your system and alerts you when any metric exceeds a user-defined threshold.

This is the refactored version of the Day 1 script, improved with functions, error handling, and better readability.

---

## What It Does

1. Prompts you for three threshold values (CPU, Disk, Memory) as percentages (0–100).
2. Reads real-time system metrics using `psutil` and `shutil`.
3. Compares each metric against your threshold and prints a status — either **normal** or **high**.

### Sample Output

```
Enter CPU threshold: 50
Enter Disk threshold: 70
Enter Memory threshold: 80
CPU usage is normal (8.3%)
Alert: Disk usage is high (75.2% > 70%)
Memory usage is normal (62.1%)
```

---

## How to Run

```bash
cd day3
pip install psutil
python system_health.py
```

---

## Code Structure

The script is organized into four functions:

| Function | Purpose |
|---|---|
| `get_threshold(prompt)` | Asks the user for a numeric threshold. Validates the input is an integer between 0–100 and retries on invalid input. |
| `get_system_metrics()` | Collects current CPU, disk, and memory usage percentages using `psutil` and `shutil`. Returns all three as a tuple. |
| `check_health(metric_name, current_value, threshold)` | Compares a single metric against its threshold and prints whether it is normal or high. |
| `system_health()` | Main function that ties everything together — collects thresholds, reads metrics, and checks health. |

### Flow Diagram

```
system_health()
  ├── get_threshold()    x3  (user input with validation)
  ├── get_system_metrics()    (reads CPU, disk, memory)
  └── check_health()     x3  (compares & prints result)
```

---

## Error Handling

| Scenario | How It's Handled |
|---|---|
| User enters non-numeric input (e.g. `abc`) | `get_threshold()` catches `ValueError`, prints a message, and re-prompts. |
| User enters a number outside 0–100 | `get_threshold()` rejects it and re-prompts. |
| OS-level error reading metrics (e.g. permission denied, missing disk) | `system_health()` catches the exception, prints the error, and exits gracefully. |

---

## Key Libraries

- **[psutil](https://pypi.org/project/psutil/)** — Cross-platform library for retrieving CPU and memory statistics.
- **[shutil](https://docs.python.org/3/library/shutil.html)** — Standard library module; `shutil.disk_usage()` returns disk space details.

---

## Improvements Over Day 1

| Area | Day 1 | Day 3 |
|---|---|---|
| Structure | All code at top level | Organized into functions |
| Input validation | None — crashes on bad input | `try/except` with retry loop |
| Error handling | None | Catches system metric errors |
| Output | Basic text | Shows actual percentages |
| Reusability | Single block | `check_health()` is reusable for any metric |
| Entry point | Runs on import | Guarded with `if __name__ == "__main__"` |
