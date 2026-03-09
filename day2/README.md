# Day 2 - Python Virtual Environments (venv)

## What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows you to install packages and dependencies specific to a project without affecting the global Python installation. Each virtual environment has its own Python binary and its own independent set of installed packages.

### Why use a virtual environment?

- **Dependency isolation** - Different projects can use different versions of the same package without conflicts.
- **Clean global environment** - Your system Python stays untouched.
- **Reproducibility** - Makes it easy to share exact dependency requirements with others.

---

## Creating and Activating a Virtual Environment

### Ubuntu / Linux

#### 1. Install the venv module (if not already installed)

```bash
sudo apt update
sudo apt install python3-venv
```

> `python3-venv` is the package that provides the `venv` module. Some minimal Ubuntu installations don't include it by default.

#### 2. Create a virtual environment

```bash
python3 -m venv env
```

- `python3` - Calls the Python 3 interpreter.
- `-m venv` - Runs the built-in `venv` module.
- `env` - Name of the folder that will hold the virtual environment. You can use any name (e.g., `.venv`, `myenv`).

This creates an `env/` directory containing:
- A copy of the Python binary
- A `pip` executable
- A `lib/` directory where installed packages will live

#### 3. Activate the virtual environment

```bash
source env/bin/activate
```

After activation, your terminal prompt changes to show the environment name:

```
(env) user@machine:~/project$
```

This tells the shell to use the Python and pip binaries inside `env/` instead of the system-wide ones.

#### 4. Deactivate the virtual environment

```bash
deactivate
```

This returns you to the global Python environment.

---

### Windows

#### 1. Verify Python is installed

```cmd
python --version
```

> The `venv` module comes bundled with the standard Python installer on Windows. No separate installation is needed.

#### 2. Create a virtual environment

**Command Prompt (cmd):**

```cmd
python -m venv env
```

**PowerShell:**

```powershell
python -m venv env
```

- `python` - Calls the Python interpreter (on Windows, `python` usually points to Python 3).
- `-m venv` - Runs the built-in `venv` module.
- `env` - Name of the folder for the virtual environment.

This creates an `env\` directory containing:
- A copy of the Python binary (`python.exe`)
- A `pip` executable
- A `Lib\` directory where installed packages will live
- A `Scripts\` directory with activation scripts

#### 3. Activate the virtual environment

**Command Prompt (cmd):**

```cmd
env\Scripts\activate.bat
```

**PowerShell:**

```powershell
env\Scripts\Activate.ps1
```

> **PowerShell Execution Policy:** If you get an error in PowerShell, you may need to allow script execution first:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**Git Bash:**

```bash
source env/Scripts/activate
```

After activation, your prompt changes to show the environment name:

```
(env) C:\Users\you\project>
```

#### 4. Deactivate the virtual environment

```cmd
deactivate
```

---

## Quick Reference

| Action | Ubuntu / Linux | Windows (cmd) | Windows (PowerShell) |
|---|---|---|---|
| Create venv | `python3 -m venv env` | `python -m venv env` | `python -m venv env` |
| Activate | `source env/bin/activate` | `env\Scripts\activate.bat` | `env\Scripts\Activate.ps1` |
| Deactivate | `deactivate` | `deactivate` | `deactivate` |

---

## Verifying the Virtual Environment is Active

Once activated, you can confirm you're using the correct Python:

```bash
which python    # Ubuntu/Linux/Git Bash
where python    # Windows cmd
```

The output should point to the `env/` directory, not the system Python path.
