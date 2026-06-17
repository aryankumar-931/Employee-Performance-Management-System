import streamlit as st
import pandas as pd

from modules.employee import (
    add_employee,
    get_all_employees,
    update_employee,
    delete_employee
)


def show_page():

    company_id = st.session_state.company_id

    st.title("👨‍💼 Employee Management")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "➕ Add Employee",
            "👀 View Employees",
            "✏️ Update Employee",
            "🗑️ Delete Employee"
        ]
    )

    # =========================
    # ADD EMPLOYEE
    # =========================

    with tab1:

        st.subheader("Add Employee")

        name = st.text_input("Name")

        department = st.text_input(
            "Department"
        )

        role = st.text_input(
            "Role"
        )

        salary = st.number_input(
            "Salary",
            min_value=0
        )

        if st.button("Add Employee"):

            add_employee(
                company_id,
                name,
                department,
                role,
                salary
            )

            st.success(
                "Employee Added Successfully!"
            )

    # =========================
    # VIEW EMPLOYEES
    # =========================

    with tab2:

        st.subheader("Employee List")

        data = get_all_employees(
            company_id
        )

        if data:

            df = pd.DataFrame(
                data,
                columns=[
                    "ID",
                    "Company ID",
                    "Name",
                    "Department",
                    "Role",
                    "Salary"
                ]
            )
            df = df.drop(
                columns=["Company ID"]
            )

            search = st.text_input(
                "Search Employee"
            )

            if search:

                df = df[
                    df["Name"].str.contains(
                        search,
                        case=False,
                        na=False
                    )
                ]

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No employees found."
            )

    # =========================
    # UPDATE EMPLOYEE
    # =========================

    with tab3:

        st.subheader(
            "Update Employee"
        )

        emp_id = st.number_input(
            "Employee ID",
            min_value=1,
            key="update_id"
        )

        new_name = st.text_input(
            "New Name"
        )

        new_department = st.text_input(
            "New Department"
        )

        new_role = st.text_input(
            "New Role"
        )

        new_salary = st.number_input(
            "New Salary",
            min_value=0
        )

        if st.button(
            "Update Employee"
        ):

            update_employee(
                emp_id,
                new_name,
                new_department,
                new_role,
                new_salary,
                company_id
            )

            st.success(
                "Employee Updated Successfully!"
            )

    # =========================
    # DELETE EMPLOYEE
    # =========================

    with tab4:

        st.subheader(
            "Delete Employee"
        )

        emp_id = st.number_input(
            "Employee ID To Delete",
            min_value=1,
            key="delete_id"
        )

        if st.button(
            "Delete Employee"
        ):

            delete_employee(
                emp_id,
                company_id
            )

            st.success(
                "Employee Deleted Successfully!"
            )