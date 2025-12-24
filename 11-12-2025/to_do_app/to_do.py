import logging
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from flask import render_template, redirect, url_for
app = Flask(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
def get_db():
    try:
        conn = mysql.connector.connect(
         



        )
        if conn.is_connected():
            return conn
        raise RuntimeError("DB connection not established")
    except Error as e:
        logging.error(f"DB connection error: {e}")
        raise


@app.route("/", methods=["GET"])
def html_tasks():
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, title, description, status,
                   DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at
            FROM tasks
            ORDER BY created_at DESC
        """)
        rows = cursor.fetchall()
        return render_template("tasks.html", tasks=rows, message=None)
    except Exception as e:
        logging.exception("Error rendering Jinja tasks page")
        return "Error rendering page", 500
    finally:
        try:
            if cursor: cursor.close()
            if db: db.close()
        except Exception:
            pass


@app.route("/html/tasks/add", methods=["POST"])
def html_add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip() or None
    if not title:
        # Reload with message
        return redirect(url_for("html_tasks"))
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
        db.commit()
        return redirect(url_for("html_tasks"))
    except Exception as e:
        logging.exception("Error in HTML add task")
        return "Add error", 500
    finally:
        try:
            if cursor: cursor.close()
            if db: db.close()
        except Exception:
            pass


# Flip status (HTML form POST)
@app.route("/html/tasks/<int:task_id>/flip", methods=["POST"])
def html_flip_task(task_id):
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT status FROM tasks WHERE id = %s", (task_id,))
        row = cursor.fetchone()
        if not row:
            return redirect(url_for("html_tasks"))
        current = row[0]
        if current not in ("Pending", "Completed"):
            return redirect(url_for("html_tasks"))
        new_status = "Completed" if current == "Pending" else "Pending"
        cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (new_status, task_id))
        db.commit()
        return redirect(url_for("html_tasks"))
    except Exception as e:
        logging.exception("Error flipping status (HTML)")
        return "Flip error", 500
    finally:
        try:
            if cursor: cursor.close()
            if db: db.close()
        except Exception:
            pass


# Edit title/description (HTML form POST)
@app.route("/html/tasks/<int:task_id>/edit", methods=["POST"])
def html_edit_task(task_id):
    title = request.form.get("title")
    description = request.form.get("description")
    updates = []
    params = []
    if title is not None:
        updates.append("title = %s"); params.append(title.strip())
    if description is not None:
        d = description.strip()
        params.append(d if d != "" else None)
        updates.append("description = %s")

    if not updates:
        return redirect(url_for("html_tasks"))

    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor()
        sql = f"UPDATE tasks SET {', '.join(updates)} WHERE id = %s"
        params.append(task_id)
        cursor.execute(sql, params)
        db.commit()
        return redirect(url_for("html_tasks"))
    except Exception as e:
        logging.exception("Error editing task (HTML)")
        return "Edit error", 500
    finally:
        try:
            if cursor: cursor.close()
            if db: db.close()
        except Exception:
            pass


# Delete (HTML form POST)
@app.route("/html/tasks/<int:task_id>/delete", methods=["POST"])
def html_delete_task(task_id):
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        db.commit()
        return redirect(url_for("html_tasks"))
    except Exception as e:
        logging.exception("Error deleting task (HTML)")
        return "Delete error", 500
    finally:
        try:
            if cursor: cursor.close()
            if db: db.close()
        except Exception:
            pass
if __name__ == "__main__":
    app.run(debug=True)