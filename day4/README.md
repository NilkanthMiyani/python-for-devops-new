# Day 4 — File Handling & Log Analysis for DevOps

A Python script that reads an application log file, counts log levels (INFO, WARNING, ERROR), prints a summary to the terminal, and writes it to a JSON output file.

---

## Files

| File | Description |
|---|---|
| `log_analyzer.py` | Main script — reads, analyzes, and summarizes logs |
| `app.log` | Sample input log file |
| `log_summary.json` | Generated output with counts per log level |

---

## How to Run

```bash
cd day4
python log_analyzer.py
```

No external dependencies — uses only the Python standard library (`json`).

---

## Sample Terminal Output

```
===== Log Analysis Summary =====
Total lines analyzed: 15
  INFO      : 10
  WARNING   : 2
  ERROR     : 3
================================

Summary written to log_summary.json
```

---

## Code Structure

| Function | Purpose |
|---|---|
| `read_log_file(filepath)` | Opens the log file and returns its lines. Raises `ValueError` if the file is empty. |
| `count_log_levels(lines)` | Iterates through lines and counts occurrences of each log level using a dictionary. |
| `print_summary(counts, total_lines)` | Formats and prints the summary to the terminal. |
| `write_summary(filepath, counts, total_lines)` | Writes the summary as a JSON file. |
| `analyze_log(input_file, output_file)` | Main function that ties the full workflow together. |

### Flow

```
analyze_log()
  ├── read_log_file()       → read lines from app.log
  ├── count_log_levels()    → count INFO / WARNING / ERROR
  ├── print_summary()       → display results in terminal
  └── write_summary()       → save results to log_summary.json
```

---

## Error Handling

| Scenario | Handling |
|---|---|
| Log file not found | Catches `FileNotFoundError`, prints a message instead of crashing. |
| Log file is empty | `read_log_file()` raises `ValueError`, caught in `__main__` with a clear message. |

---

## Concepts Covered

- File read operations (`open`, `readlines`)
- String searching to identify log levels
- Dictionaries for counting
- JSON output with `json.dump`
- Functions for clean separation of logic
- `try / except` for error handling
