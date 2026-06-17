from database.db import get_connection


def add_employee(
    company_id,
    name,
    department,
    role,
    salary
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees
    (
        company_id,
        name,
        department,
        role,
        salary
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        company_id,
        name,
        department,
        role,
        salary
    ))

    conn.commit()
    conn.close()


def get_all_employees(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM employees
    WHERE company_id = ?
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_employee_names(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, name
    FROM employees
    WHERE company_id = ?
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def delete_employee(
    emp_id,
    company_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM employees
    WHERE id = ?
    AND company_id = ?
    """,
    (
        emp_id,
        company_id
    ))

    conn.commit()
    conn.close()


def update_employee(
    emp_id,
    name,
    department,
    role,
    salary,
    company_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employees
    SET
        name = ?,
        department = ?,
        role = ?,
        salary = ?
    WHERE id = ?
    AND company_id = ?
    """,
    (
        name,
        department,
        role,
        salary,
        emp_id,
        company_id
    ))

    conn.commit()
    conn.close()


def get_employee_count(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM employees
    WHERE company_id = ?
    """,
    (company_id,))

    count = cursor.fetchone()[0]

    conn.close()

    return count