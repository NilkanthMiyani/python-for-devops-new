import json


LOG_LEVELS = ["INFO", "WARNING", "ERROR"]


def read_log_file(filepath):
    """Read a log file and return its lines."""
    with open(filepath, "r") as f:
        lines = f.readlines()
    if not lines:
        raise ValueError(f"Log file '{filepath}' is empty.")
    return lines


def count_log_levels(lines):
    """Count occurrences of each log level in the given lines."""
    counts = {level: 0 for level in LOG_LEVELS}
    for line in lines:
        for level in LOG_LEVELS:
            if f" {level} " in line:
                counts[level] += 1
                break
    return counts


def print_summary(counts, total_lines):
    """Print the log summary to the terminal."""
    print("\n===== Log Analysis Summary =====")
    print(f"Total lines analyzed: {total_lines}")
    for level, count in counts.items():
        print(f"  {level:10s}: {count}")
    print("================================\n")


def write_summary(filepath, counts, total_lines):
    """Write the log summary to a JSON output file."""
    summary = {
        "total_lines": total_lines,
        "counts": counts,
    }
    with open(filepath, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary written to {filepath}")


def analyze_log(input_file, output_file):
    """Main function: read log, count levels, print & write summary."""
    lines = read_log_file(input_file)
    total_lines = len([line for line in lines if line.strip()])
    counts = count_log_levels(lines)
    print_summary(counts, total_lines)
    write_summary(output_file, counts, total_lines)


if __name__ == "__main__":
    input_path = "app.log"
    output_path = "log_summary.json"

    try:
        analyze_log(input_path, output_path)
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
