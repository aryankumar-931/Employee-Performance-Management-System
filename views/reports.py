import streamlit as st
import pandas as pd
from io import BytesIO

from modules.employee import get_all_employees
from modules.performance import get_performance


def convert_df_to_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Report"
        )

    return output.getvalue()


def show_page():

    company_id = st.session_state.company_id

    st.title("📄 Reports")
    st.caption(
        "Generate and download employee reports"
    )

    tab1, tab2 = st.tabs(
        [
            "👨 Employee Report",
            "📈 Performance Report"
        ]
    )

    # =========================
    # EMPLOYEE REPORT
    # =========================

    with tab1:

        st.subheader(
            "👨 Employee Report"
        )

        employees = get_all_employees(
            company_id
        )

        if employees:

            employee_df = pd.DataFrame(
                employees,
                columns=[
                    "ID",
                    "Company ID",
                    "Name",
                    "Department",
                    "Role",
                    "Salary"
                ]
            )

            # Company ID hide
            employee_df = employee_df.drop(
                columns=["Company ID"]
            )

            departments = (
                ["All"] +
                sorted(
                    employee_df[
                        "Department"
                    ].unique().tolist()
                )
            )

            selected_department = st.selectbox(
                "Filter by Department",
                departments
            )

            if selected_department != "All":

                employee_df = employee_df[
                    employee_df["Department"]
                    == selected_department
                ]

            st.dataframe(
                employee_df,
                use_container_width=True
            )

            csv = employee_df.to_csv(
                index=False
            )

            st.download_button(
                label="⬇ Download CSV",
                data=csv,
                file_name="employee_report.csv",
                mime="text/csv"
            )

            excel_data = convert_df_to_excel(
                employee_df
            )

            st.download_button(
                label="📊 Download Excel",
                data=excel_data,
                file_name="employee_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        else:

            st.warning(
                "No employee data found."
            )

    # =========================
    # PERFORMANCE REPORT
    # =========================

    with tab2:

        st.subheader(
            "📈 Performance Report"
        )

        performance_data = get_performance(
            company_id
        )

        if performance_data:

            performance_df = pd.DataFrame(
                performance_data,
                columns=[
                    "Employee",
                    "Attendance",
                    "Task Completion",
                    "Quality Score",
                    "Manager Feedback",
                    "Performance Score",
                    "Rating"
                ]
            )

            ratings = (
                ["All"] +
                sorted(
                    performance_df[
                        "Rating"
                    ].unique().tolist()
                )
            )

            selected_rating = st.selectbox(
                "Filter by Rating",
                ratings
            )

            if selected_rating != "All":

                performance_df = performance_df[
                    performance_df["Rating"]
                    == selected_rating
                ]

            st.dataframe(
                performance_df,
                use_container_width=True
            )

            csv = performance_df.to_csv(
                index=False
            )

            st.download_button(
                label="⬇ Download CSV",
                data=csv,
                file_name="performance_report.csv",
                mime="text/csv"
            )

            excel_data = convert_df_to_excel(
                performance_df
            )

            st.download_button(
                label="📊 Download Excel",
                data=excel_data,
                file_name="performance_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        else:

            st.warning(
                "No performance data found."
            )
