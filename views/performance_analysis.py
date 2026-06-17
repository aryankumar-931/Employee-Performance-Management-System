import streamlit as st
import pandas as pd

from modules.employee import get_employee_names

from modules.performance import (
    calculate_score,
    add_performance,
    get_performance,
    get_top_performers
)


def show_page():

    company_id = st.session_state.company_id

    st.title("📈 Performance Analysis")

    tab1, tab2, tab3 = st.tabs(
        [
            "➕ Add Performance",
            "📈 View Performance",
            "🏆 Top Performers"
        ]
    )

    # ==================================
    # TAB 1 : ADD PERFORMANCE
    # ==================================

    with tab1:

        st.subheader("Add Employee Performance")

        employees = get_employee_names(
            company_id
        )

        if not employees:

            st.warning(
                "No employees found. Please add employees first."
            )

            return

        employee_dict = {
            emp[1]: emp[0]
            for emp in employees
        }

        selected_employee = st.selectbox(
            "Select Employee",
            list(employee_dict.keys())
        )

        attendance = st.slider(
            "Attendance",
            0,
            100,
            80
        )

        task_completion = st.slider(
            "Task Completion",
            0,
            100,
            80
        )

        quality_score = st.slider(
            "Quality Score",
            0,
            100,
            80
        )

        manager_feedback = st.slider(
            "Manager Feedback",
            0,
            100,
            80
        )

        if st.button(
            "Calculate & Save"
        ):

            score, rating = calculate_score(
                attendance,
                task_completion,
                quality_score,
                manager_feedback
            )

            add_performance(
                company_id,
                employee_dict[selected_employee],
                attendance,
                task_completion,
                quality_score,
                manager_feedback,
                score,
                rating
            )

            st.success(
                f"Performance Saved Successfully! | Score: {score} | Rating: {rating}"
            )

    # ==================================
    # TAB 2 : VIEW PERFORMANCE
    # ==================================

    with tab2:

        st.subheader(
            "📈 View Performance Records"
        )

        data = get_performance(
            company_id
        )

        if data:

            df = pd.DataFrame(
                data,
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

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.warning(
                "No performance records found."
            )

    # ==================================
    # TAB 3 : TOP PERFORMERS
    # ==================================

    with tab3:

        st.subheader(
            "🏆 Top Performers"
        )

        top_data = get_top_performers(
            company_id
        )

        if top_data:

            for index, employee in enumerate(
                top_data
            ):

                if index == 0:
                    medal = "🥇"

                elif index == 1:
                    medal = "🥈"

                elif index == 2:
                    medal = "🥉"

                else:
                    medal = "🏅"

                st.success(
                    f"{medal} {employee[0]} | Score: {employee[1]}"
                )

        else:

            st.warning(
                "No performance data available."
            )