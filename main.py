#!/usr/bin/env python3
import sys
import sqlite3
import os
from pathlib import Path
from datetime import datetime


def get_database_path():
    """Get the path to the SQLite database in the user's home directory."""
    home_dir = Path.home()
    pytasks_dir = home_dir / ".pytasks"
    pytasks_dir.mkdir(exist_ok=True)
    return pytasks_dir / "tasks.db"


def init_database():
    """Initialize the SQLite database with the tasks table."""
    db_path = get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_string TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()


def store_task(task_string):
    """Store a task string in the database."""
    db_path = get_database_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO tasks (task_string) VALUES (?)",
        (task_string,)
    )
    
    conn.commit()
    conn.close()
    print(f"Task stored: {task_string}")


def list_tasks():
    """List all stored tasks from the database."""
    db_path = get_database_path()
    
    if not db_path.exists():
        print("No tasks found.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT id, task_string, created_at FROM tasks ORDER BY created_at DESC"
    )
    
    tasks = cursor.fetchall()
    conn.close()
    
    if not tasks:
        print("No tasks found.")
        return
    
    print("Stored tasks:")
    print("-" * 60)
    for task_id, task_string, created_at in tasks:
        # Parse the timestamp and format it nicely
        dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{task_id:3d}] {formatted_time} | {task_string}")


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <task_string>")
        print("       python main.py ls")
        sys.exit(1)
    
    # Initialize database
    init_database()
    
    # Get the argument
    argument = sys.argv[1]
    
    if argument == "ls":
        list_tasks()
    else:
        # Join all arguments after the first one to allow multi-word tasks
        task_string = " ".join(sys.argv[1:])
        store_task(task_string)


if __name__ == "__main__":
    main()