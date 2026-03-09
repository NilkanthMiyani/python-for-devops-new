# Day 2 - Python for DevOps

## Topics Covered

1. [Virtual Environments (venv)](#1-virtual-environments-venv)
2. [Data Structures - Lists](#2-data-structures---lists)
3. [Data Structures - Dictionaries](#3-data-structures---dictionaries)
4. [Data Structures - Sets](#4-data-structures---sets)
5. [File Handling (Read/Write)](#5-file-handling-readwrite)
6. [Working with APIs](#6-working-with-apis)
7. [Saving JSON Output to Files](#7-saving-json-output-to-files)

---

## 1. Virtual Environments (venv)

A virtual environment is an isolated Python environment that allows you to install packages and dependencies specific to a project without affecting the global Python installation.

### Why use a virtual environment?

- **Dependency isolation** - Different projects can use different versions of the same package without conflicts.
- **Clean global environment** - Your system Python stays untouched.
- **Reproducibility** - Makes it easy to share exact dependency requirements with others.

### Quick Reference

| Action | Ubuntu / Linux | Windows (cmd) | Windows (PowerShell) |
|---|---|---|---|
| Create venv | `python3 -m venv env` | `python -m venv env` | `python -m venv env` |
| Activate | `source env/bin/activate` | `env\Scripts\activate.bat` | `env\Scripts\Activate.ps1` |
| Deactivate | `deactivate` | `deactivate` | `deactivate` |

> **PowerShell Execution Policy:** If you get an error in PowerShell, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**File:** No script — setup done via terminal commands.

---

## 2. Data Structures - Lists

Lists are ordered, mutable collections that can hold mixed data types.

### Key concepts covered (`list_ex.py`)

- Creating lists with mixed types: `[100, 200, 'nilkanth', True, 4.5]`
- Creating empty lists: `list()`
- Adding items: `.append()`
- Accessing by index: `clouds[0]`
- Exploring methods: `dir()` and `.__doc__`
- Iterating with `for` loop and `if/elif/else`

```python
clouds = list()
clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")

for cloud in clouds:
    if cloud == "aws":
        print("Amazon is the market leader")
```

---

## 3. Data Structures - Dictionaries

Dictionaries are key-value pairs, useful for storing structured data.

### Key concepts covered (`dict_ex.py`)

- Creating dicts with nested types (strings, integers, booleans, lists)
- Accessing values: `info["city"]` vs `info.get("key", "default")`
- Updating values: `.update()`
- Iterating keys only vs key-value pairs: `.items()`

```python
info = {
    "name": "Nilkanth",
    "age": 30,
    "city": "Surat"
}

for key, value in info.items():
    print(key, ':', value)
```

---

## 4. Data Structures - Sets

Sets are unordered collections that do not allow duplicate values.

### Key concepts covered (`set_ex.py`)

- Creating empty sets: `set()`
- Duplicate removal: `{"saturday", "sunday", "saturday"}` results in only 2 items
- Converting a list to a set and back to remove duplicates

```python
nums = [1, 1, 1, 2, 222, 2, 5023.1]
nums = list(set(nums))  # removes duplicates
```

---

## 5. File Handling (Read/Write)

Basic file operations in Python using `open()`.

### Key concepts covered (`read_write_files.py`)

- Opening a file: `open("demo.txt")`
- Reading contents: `file.read()`
- Writing to a file: `file.write()`
- Closing a file: `file.close()`

```python
file = open("demo.txt")
print(file.read())
file.close()
```

---

## 6. Working with APIs

Using the `requests` library to interact with REST APIs and parse JSON responses.

### Key concepts covered

#### Basic API call (`api.py`)

- Sending GET requests: `requests.get(url=api_url)`
- Parsing JSON responses: `response.json()`
- Iterating over response data and applying conditional logic

#### Jokes API (`jokes_api.py`)

- Setting custom headers: `{"Accept": "application/json"}`
- Using `input()` for user interaction
- Defining functions to handle API logic
- Conditional URL selection based on user input

#### Stock Market API (`stock_market_api.py`)

- Using API keys for authentication
- Building dynamic query strings with f-strings
- Working with time series data from Alpha Vantage API

---

## 7. Saving JSON Output to Files

Persisting API responses to JSON files using the `json` module, with append support so previous data is not lost.

### Key concepts covered (in `jokes_api.py` and `stock_market_api.py`)

- `import json` - built-in module for JSON handling
- `json.load()` - read JSON from a file into Python objects
- `json.dump()` - write Python objects to a file as JSON
- `try/except` - handle `FileNotFoundError` and `json.JSONDecodeError`
- `isinstance()` - check data type before operating on it
- Appending to a JSON list without overwriting existing data

```python
filename = "output.json"
try:
    with open(filename, "r") as f:
        existing_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    existing_data = []

if isinstance(existing_data, dict):
    existing_data = [existing_data]

existing_data.append(new_data)

with open(filename, "w") as f:
    json.dump(existing_data, f, indent=4)
```

---

## Files Overview

| File | Description |
|---|---|
| `list_ex.py` | List operations and iteration |
| `dict_ex.py` | Dictionary operations and iteration |
| `set_ex.py` | Set basics and duplicate removal |
| `read_write_files.py` | Basic file read/write operations |
| `api.py` | Simple REST API call with `requests` |
| `jokes_api.py` | Jokes API with JSON output saved to file |
| `stock_market_api.py` | Stock market API with JSON output saved to file |
| `demo.txt` | Sample text file for file handling practice |
