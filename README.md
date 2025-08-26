# 📝 pytasks

Simple command line tool to store and list tasks as strings in SQLite database.

## Requirements

🐍 **Python 3.12+** (uses standard library only)

## Usage

📥 **Store a task:**
```bash
uv run main.py "your task here"
```

📋 **List all tasks:**
```bash
uv run main.py ls
```

🗄️ Database stored in `~/.pytasks/tasks.db`
