from database.db import get_connection


def create_task(title: str, description: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (title, description)
    )

    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return get_task(task_id)


def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    return [dict(row) for row in rows]


def get_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    row = cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()
    conn.close()

    return dict(row) if row else None


def update_task(task_id: int, title: str, description: str | None, completed: bool):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?, completed = ?
        WHERE id = ?
    """, (title, description, int(completed), task_id))

    conn.commit()
    conn.close()

    return get_task(task_id)


def delete_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()