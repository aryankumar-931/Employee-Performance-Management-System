from database.db import get_connection


def calculate_score(
    attendance,
    task_completion,
    quality_score,
    manager_feedback
):

    score = (
        attendance * 0.25 +
        task_completion * 0.35 +
        quality_score * 0.25 +
        manager_feedback * 0.15
    )

    if score >= 85:
        rating = "Excellent"

    elif score >= 70:
        rating = "Good"

    else:
        rating = "Needs Improvement"

    return round(score, 2), rating


def add_performance(
    company_id,
    employee_id,
    attendance,
    task_completion,
    quality_score,
    manager_feedback,
    performance_score,
    rating
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO performance
    (
        company_id,
        employee_id,
        attendance,
        task_completion,
        quality_score,
        manager_feedback,
        performance_score,
        rating
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        company_id,
        employee_id,
        attendance,
        task_completion,
        quality_score,
        manager_feedback,
        performance_score,
        rating
    ))

    conn.commit()
    conn.close()


def get_performance(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        employees.name,
        performance.attendance,
        performance.task_completion,
        performance.quality_score,
        performance.manager_feedback,
        performance.performance_score,
        performance.rating
    FROM performance
    JOIN employees
    ON performance.employee_id = employees.id
    WHERE performance.company_id = ?
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_top_performers(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        employees.name,
        performance.performance_score
    FROM performance
    JOIN employees
    ON performance.employee_id = employees.id
    WHERE performance.company_id = ?
    ORDER BY performance.performance_score DESC
    LIMIT 5
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_average_score(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(performance_score)
    FROM performance
    WHERE company_id = ?
    """,
    (company_id,))

    result = cursor.fetchone()[0]

    conn.close()

    return round(result, 2) if result else 0


def get_excellent_count(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM performance
    WHERE company_id = ?
    AND rating = 'Excellent'
    """,
    (company_id,))

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_top_performer(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        employees.name,
        performance.performance_score
    FROM performance
    JOIN employees
    ON employees.id = performance.employee_id
    WHERE performance.company_id = ?
    ORDER BY performance.performance_score DESC
    LIMIT 1
    """,
    (company_id,))

    result = cursor.fetchone()

    conn.close()

    return result


def get_rating_distribution(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        rating,
        COUNT(*)
    FROM performance
    WHERE company_id = ?
    GROUP BY rating
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_top_performers_chart(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        employees.name,
        performance.performance_score
    FROM performance
    JOIN employees
    ON employees.id = performance.employee_id
    WHERE performance.company_id = ?
    ORDER BY performance.performance_score DESC
    LIMIT 5
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_department_performance(company_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        employees.department,
        AVG(performance.performance_score)
    FROM performance
    JOIN employees
    ON employees.id = performance.employee_id
    WHERE performance.company_id = ?
    GROUP BY employees.department
    """,
    (company_id,))

    data = cursor.fetchall()

    conn.close()

    return data


def get_employee_performance(
    employee_name,
    company_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        performance.attendance,
        performance.task_completion,
        performance.quality_score,
        performance.manager_feedback,
        performance.performance_score,
        performance.rating
    FROM performance
    JOIN employees
    ON performance.employee_id = employees.id
    WHERE employees.name = ?
    AND performance.company_id = ?
    ORDER BY performance.id DESC
    LIMIT 1
    """,
    (
        employee_name,
        company_id
    ))

    data = cursor.fetchone()

    conn.close()

    return data