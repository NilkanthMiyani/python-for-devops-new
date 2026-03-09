# Day 1 - Python for DevOps

## Topics Covered

1. [Variables, Constants and Data Types](#1-variables-constants-and-data-types)
2. [Operators](#2-operators)
3. [User Input](#3-user-input)
4. [Conditional Statements (if/elif/else)](#4-conditional-statements-ifelifelse)
5. [Loops (for and while)](#5-loops-for-and-while)
6. [String Formatting (f-strings)](#6-string-formatting-f-strings)
7. [Functions](#7-functions)
8. [Importing Libraries](#8-importing-libraries)
9. [System Health Monitoring](#9-system-health-monitoring)

---

## 1. Variables, Constants and Data Types

Variables hold values that can change. Constants are fixed values like numbers or strings.

### Key concepts covered (`my_first_file.py`)

- Variable assignment using `=` (assignment operator)
- Reassigning variables
- Data types: `int`, `float`, `str`, `bool`
- Checking type with `type()`

```python
a = 100
env = "dev"
print(type(a))  # <class 'int'>
```

---

## 2. Operators

Operators perform operations on values (operands).

### Key concepts covered (`my_first_file.py`)

- Arithmetic operators: `+`, `-`, `*`, `/`
- Operands: the values being operated on (e.g., `a` and `b`)
- Operation: the full expression (e.g., `a + b`)

```python
x = 50
y = 20
z = x * y
print("z is", z)  # z is 1000
```

---

## 3. User Input

Getting input from the user at runtime using `input()`.

### Key concepts covered (`check_env.py`)

- `input()` returns a string
- `int(input())` to convert input to integer
- Using input values in calculations and conditions

```python
env = input("Enter the env: ")
a = int(input("Enter the num 1: "))
```

---

## 4. Conditional Statements (if/elif/else)

Execute different code blocks based on conditions.

### Key concepts covered (`check_env.py`)

- `if` - check a condition
- `elif` - check another condition if the first is false
- `else` - fallback when no conditions match
- Comparison operator: `==`

```python
if env == "prod":
    print("Never deploy on friday!")
elif env == "stg":
    print("Test Well, before prod")
else:
    print("dev is the best env to work on")
```

---

## 5. Loops (for and while)

Repeat a block of code multiple times.

### Key concepts covered (`loop_test.py`, `tables_test.py`)

- `for` loop with `range()` to repeat a fixed number of times
- `while` loop to repeat until a condition is met
- `break` to exit a loop early
- Nested loops (for inside while)

```python
# for loop
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# while loop with quit option
choice = input("Enter the choice (press q to quit): ")
while choice != "q":
    # do work
    choice = input("Enter the choice (press q to quit): ")
```

---

## 6. String Formatting (f-strings)

Insert variables directly into strings using `f""` syntax.

### Key concepts covered (`tables_test.py`)

- Prefix string with `f`
- Place variables inside `{}`
- Expressions inside `{}` are evaluated

```python
name = "Nilkanth"
print(f"Hello {name}, welcome to python for devops class!")
```

---

## 7. Functions

Functions group reusable blocks of code under a name.

### Key concepts covered (`functions_test.py`)

- Defining a function: `def function_name():`
- Calling a function: `function_name()`
- Functions contain steps (instructions)
- Calling functions conditionally

```python
def sum_of_num():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    print(num1 + num2)

if env == "prd":
    sum_of_num()
```

---

## 8. Importing Libraries

Using external libraries to extend Python's capabilities.

### Key concepts covered (`check_cpu.py`)

- `import` statement to bring in external packages
- `psutil` - library for system/process utilities (installed from PyPI)
- `psutil.cpu_percent()` to get current CPU usage

```python
import psutil

current_cpu = psutil.cpu_percent(interval=1)
```

---

## 9. System Health Monitoring

A practical DevOps use case combining all Day 1 concepts.

### Key concepts covered (`system_health.py`)

- Monitoring CPU, disk, and memory usage
- Using `psutil` for CPU and memory metrics
- Using `shutil.disk_usage()` for disk metrics
- Comparing system metrics against user-defined thresholds
- Alerting when thresholds are exceeded

```python
import psutil
import shutil

cpu = psutil.cpu_percent(interval=1)
disk = (shutil.disk_usage('C:/').used / shutil.disk_usage('C:/').total) * 100
memory = psutil.virtual_memory().percent

if cpu > cpu_threshold:
    print("Alert: CPU usage is high")
```

---

## Files Overview

| File | Description |
|---|---|
| `my_first_file.py` | Variables, data types, operators, and `print()` |
| `check_env.py` | User input and conditional statements |
| `loop_test.py` | `for` loop with `range()` and conditionals |
| `tables_test.py` | `while` loop, nested `for` loop, f-strings |
| `functions_test.py` | Function definition and calling |
| `check_cpu.py` | CPU monitoring with `psutil` |
| `system_health.py` | Full system health check (CPU, disk, memory) |
