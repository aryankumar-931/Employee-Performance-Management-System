import hashlib

from database.db import get_connection


def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def register_admin(
    company_name,
    username,
    password,
    role="Admin"
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO admins
        (
            company_name,
            username,
            password,
            role
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            company_name,
            username,
            hash_password(password),
            role
        ))

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def login(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM admins
    WHERE username=?
    AND password=?
    """,
    (
        username,
        hash_password(password)
    ))

    user = cursor.fetchone()

    conn.close()

    return user


def change_password(
    username,
    new_password
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE admins
    SET password=?
    WHERE username=?
    """,
    (
        hash_password(new_password),
        username
    ))

    conn.commit()
    conn.close()