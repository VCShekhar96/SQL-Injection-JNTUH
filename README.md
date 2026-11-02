# SQL Injection Demonstration – Vulnerable vs Secure Login

A hands-on educational project demonstrating **SQL Injection (SQLi)** through a Python Flask web application and SQLite database. This project compares an intentionally vulnerable authentication mechanism with a secure implementation using parameterized SQL queries.

> **Educational Use Only:** The vulnerable login is intentionally insecure and is designed exclusively for a controlled local learning environment. Do not deploy this application to a public-facing server or use it against systems without explicit authorization.

---

## 1. Project Overview

SQL Injection is a web application security vulnerability that occurs when untrusted user input is incorporated into SQL statements without proper handling.

This project demonstrates how an attacker can manipulate a vulnerable SQL query through specially crafted input and how parameterized queries prevent this type of SQL injection.

The application provides two authentication modes through a single login interface:

- **Vulnerable Login:** Uses dynamically constructed SQL queries through Python string formatting.
- **Secure Login:** Uses parameterized SQL queries to separate user input from SQL commands.

The objective is to understand the vulnerability practically and learn how to prevent it.

## 2. Project Objectives

- Understand the fundamentals of SQL Injection.
- Demonstrate how SQL Injection affects authentication systems.
- Identify the security risks of dynamically constructed SQL queries.
- Compare vulnerable and secure authentication implementations.
- Understand the role of parameterized queries in SQL security.
- Gain practical experience with Python, Flask, SQLite and web application development.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| SQLite | Database management |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| SQL | Database queries |
| Jinja2 | Dynamic HTML rendering |
| Git | Version control |
| GitHub | Source code hosting |

## 4. Project Architecture

The application follows a simple client-server architecture.

1. The user opens the login page.
2. The user enters a username and password.
3. The user selects Vulnerable Login or Secure Login.
4. Flask receives the submitted form data.
5. Python executes the corresponding SQL query against SQLite.
6. The application processes the database response.
7. The authentication result is displayed on the webpage.

## 5. Project Structure

```text
Login for SQL injection/
│
├── app.py
│
├── database.db          # Generated automatically at runtime
│
├── .gitignore
│
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

**Note:** `database.db` is generated automatically when the application initializes. It is excluded from Git using `.gitignore`.

## 6. Prerequisites

Before running the project, install:

- Windows 10/11 or another supported operating system.
- Python 3.9 or later.
- Git (optional, for cloning and version control).
- Visual Studio Code or another code editor.
- A modern web browser.

Python's built-in `sqlite3` module is used, so a separate SQLite installation is not required.

## 7. Installation and Setup

### Step 1: Clone the repository

Open PowerShell or the VS Code terminal.

```powershell
git clone https://github.com/VCShekhar96/SQL-Injection-JNTUH.git
```

Navigate into the project directory:

```powershell
cd SQL-Injection-JNTUH
```

### Step 2: Create a virtual environment

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### Step 3: Install Flask

```powershell
python -m pip install flask
```

### Step 4: Run the application

```powershell
python app.py
```

The Flask application will start locally.

Open the following URL in your browser:

**http://127.0.0.1:5000**

## 8. Sample Database Credentials

The application automatically initializes a SQLite database and inserts two sample accounts.

| Username | Password |
|---|---|
| admin | admin123 |
| alice | alice123 |

These credentials are intended only for local demonstration and testing.

## 9. Practical SQL Injection Demonstration

### Test 1: Normal Authentication

Select **Vulnerable Login** or **Secure Login**.

Enter:

Username:
```text
admin
```

Password:
```text
admin123
```

Expected result:

```text
Login successful!
```

Both authentication modes should accept valid credentials.

### Test 2: SQL Injection – Vulnerable Login

Select **Vulnerable Login**.

Enter the following username:

```sql
' OR '1'='1' -- 
```

Enter any non-empty password, for example:

```text
anything
```

Expected result:

```text
Login successful!
```

The vulnerable query becomes logically equivalent to:

```sql
SELECT username FROM users
WHERE username = '' OR '1'='1' -- '
AND password = 'anything'
```

**Explanation:**

- The single quote modifies the original SQL expression.
- `OR '1'='1'` introduces a condition that is always true.
- `--` starts an SQL comment, causing the remaining portion of the query to be ignored in SQLite.
- Consequently, the query can return the stored user records without valid credentials.

### Test 3: Same Input – Secure Login

Select **Secure Login**.

Enter the same username:

```sql
' OR '1'='1' -- 
```

Password:

```text
anything
```

Expected result:

```text
Login failed!
```

The secure implementation treats the supplied input as data rather than executable SQL syntax.

## 10. Vulnerable vs Secure SQL Implementation

### Vulnerable implementation

```python
query = (
    f"SELECT username FROM users "
    f"WHERE username = '{username}' "
    f"AND password = '{password}'"
)

rows = con.execute(query).fetchall()
```

**Security problem:**

User input is directly inserted into the SQL statement. Special SQL characters can change the query's intended logic.

### Secure implementation

```python
query = """
    SELECT username FROM users
    WHERE username = ? AND password = ?
"""

rows = con.execute(
    query, (username, password)
).fetchall()
```

**Security advantage:**

- Uses parameterized queries.
- Separates SQL commands from user-supplied values.
- Prevents input from changing the structure of the SQL statement.
- Provides protection against this class of SQL Injection vulnerability.

**Important:** Parameterized queries are essential, but production authentication systems also require password hashing, secure session management, input validation and other security controls. This demonstration stores sample passwords in plaintext for simplicity and must not be treated as production-ready authentication.

## 11. Security Concepts Demonstrated

This project illustrates:

1. SQL Injection vulnerability.
2. Authentication bypass.
3. Dynamic SQL query construction.
4. SQL comments and logical operators.
5. Parameterized SQL queries.
6. Secure database interaction.
7. Difference between trusted SQL syntax and untrusted user input.

## 12. Troubleshooting

| Problem | Possible solution |
|---|---|
| Python is not recognized | Install Python and enable Add Python to PATH |
| Flask module not found | Run `python -m pip install flask` |
| Port 5000 already in use | Stop the other application using that port |
| Database table not found | Run the application using `python app.py` so database initialization executes |
| PowerShell blocks virtual environment activation | Use the Command Prompt activation command |
| Login fails with normal credentials | Check the username and password against the sample credentials |

## 13. Limitations

- Uses SQLite for a small educational demonstration.
- Stores sample passwords in plaintext.
- Does not implement production-grade authentication.
- Does not include user registration or password recovery.
- The vulnerable implementation is intentionally insecure.
- The application is intended for local testing and learning, not production deployment.

## 14. Future Enhancements

Possible improvements include:

- Password hashing using Werkzeug or bcrypt.
- User registration and logout functionality.
- Session-based authentication.
- Improved input validation.
- Database security enhancements.
- Demonstration of additional SQL Injection techniques in isolated lab environments.
- Automated security testing.
- A more advanced user interface.

## 15. Responsible Use and Disclaimer

This project is developed strictly for academic, educational and authorized cybersecurity learning purposes.

The vulnerable login mode intentionally demonstrates insecure SQL query construction.

- Run the application only in a controlled local environment.
- Do not deploy the vulnerable version to the internet.
- Do not test SQL Injection against systems without explicit permission.
- Do not use this demonstration to access unauthorized data or systems.

The author assumes no responsibility for misuse of this educational demonstration.

## 16. Author and Repository

**Project:** SQL Injection Demonstration – Vulnerable vs Secure Login

**Repository:**  
https://github.com/VCShekhar96/SQL-Injection-JNTUH

**Developed using:** Python, Flask, SQLite, HTML and CSS.

---

*This project is intended to build practical understanding of web application security and secure database programming.*