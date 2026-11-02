
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DB = "database.db"


def init_db():
    with sqlite3.connect(DB) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        con.executemany("""
            INSERT OR IGNORE INTO users (username, password)
            VALUES (?, ?)
        """, [
            ("admin", "admin123"),
            ("alice", "alice123")
        ])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username", "")
    password = request.form.get("password", "")
    mode = request.form.get("mode", "")

    if mode not in ("vulnerable", "secure"):
        return "Invalid login mode", 400

    try:
        with sqlite3.connect(DB) as con:

            if mode == "vulnerable":

                # Intentionally unsafe: local lab only
                query = (
                    f"SELECT username FROM users "
                    f"WHERE username = '{username}' "
                    f"AND password = '{password}'"
                )

                print("[LAB] Vulnerable query:", repr(query))
                rows = con.execute(query).fetchall()

            else:

                # Secure parameterized query
                query = """
                    SELECT username FROM users
                    WHERE username = ? AND password = ?
                """

                rows = con.execute(
                    query, (username, password)
                ).fetchall()

                print("[LAB] Secure query executed.")
                print("[LAB] Secure result:", rows)

        return render_template(
            "result.html",
            message="Login successful!" if rows else "Login failed!",
            users=[row[0] for row in rows],
            mode=mode
        )

    except sqlite3.Error as error:

        print("[DATABASE ERROR]", error)

        return render_template(
            "result.html",
            message="Database query error!",
            users=[],
            mode=mode
        ), 400


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)
