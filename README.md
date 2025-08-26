# 📝 pytasks

Simple command line tool to store and list tasks as strings in SQLite database.

## Requirements

🐍 **Python 3.12+** (uses standard library only)

## Usage

📥 **Store a task:**
```bash
python3 pytasks.py "your task here"
```

📋 **List all tasks:**
```bash
python3 pytasks.py ls
```

🗑️ **Delete a task by ID:**
```bash
python3 pytasks.py rm <id>
```

🗄️ Database stored in `~/.pytasks/tasks.db`
