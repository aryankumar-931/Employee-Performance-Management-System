import sqlite3


def get_connection():

    conn = sqlite3.connect("employees.db")

    return conn


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    # =========================
    # Admins Table
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company_name TEXT NOT NULL,

        username TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        role TEXT DEFAULT 'Admin'
    )
    """)

    # =========================
    # Employees Table
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company_id INTEGER,

        name TEXT NOT NULL,

        department TEXT,

        role TEXT,

        salary INTEGER,

        FOREIGN KEY (company_id)
        REFERENCES admins(id)
    )
    """)

    # =========================
    # Performance Table
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS performance (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company_id INTEGER,

        employee_id INTEGER,

        attendance INTEGER,

        task_completion INTEGER,

        quality_score INTEGER,

        manager_feedback INTEGER,

        performance_score REAL,

        rating TEXT,

        FOREIGN KEY (company_id)
        REFERENCES admins(id),

        FOREIGN KEY (employee_id)
        REFERENCES employees(id)
    )
    """)

    conn.commit()
    conn.close()