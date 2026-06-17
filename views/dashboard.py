import streamlit as st
import pandas as pd

from modules.employee import get_employee_count

from modules.performance import (
    get_average_score,
    get_excellent_count,
    get_top_performer,
    get_top_performers,
    get_rating_distribution,
    get_top_performers_chart,
    get_department_performance
)


def show_page():

    company_id = st.session_state.company_id

    st.markdown("""
    # 📊 Dashboard

    ### Employee Performance Analytics
    """)

    total_employees = get_employee_count(
        company_id
    )

    avg_score = get_average_score(
        company_id
    )

    excellent_count = get_excellent_count(
        company_id
    )

    top_performer = get_top_performer(
        company_id
    )

    # =========================
    # KPI CARDS
    # =========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        with st.container(border=True):

            st.metric(
                "👨 Total Employees",
                total_employees
            )

    with col2:

        with st.container(border=True):

            st.metric(
                "📈 Avg Score",
                avg_score
            )

    with col3:

        with st.container(border=True):

            if top_performer:

                st.metric(
                    "🏆 Top Performer",
                    top_performer[0]
                )

            else:

                st.metric(
                    "🏆 Top Performer",
                    "-"
                )

    with col4:

        with st.container(border=True):

            st.metric(
                "⭐ Excellent",
                excellent_count
            )

    st.divider()

    # =========================
    # TOP 5 PERFORMERS
    # =========================

    with st.container(border=True):

        st.subheader(
            "🏆 Top 5 Performers"
        )

        top_data = get_top_performers(
            company_id
        )

        if top_data:

            for index, employee in enumerate(top_data):

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

    st.divider()

    # =========================
    # CHARTS
    # =========================

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader(
                "📊 Top 5 Performers Chart"
            )

            chart_data = get_top_performers_chart(
                company_id
            )

            if chart_data:

                df = pd.DataFrame(
                    chart_data,
                    columns=[
                        "Employee",
                        "Score"
                    ]
                )

                st.bar_chart(
                    df.set_index(
                        "Employee"
                    )
                )

    with col2:

        with st.container(border=True):

            st.subheader(
                "📈 Rating Distribution"
            )

            rating_data = get_rating_distribution(
                company_id
            )

            if rating_data:

                rating_df = pd.DataFrame(
                    rating_data,
                    columns=[
                        "Rating",
                        "Count"
                    ]
                )

                st.bar_chart(
                    rating_df.set_index(
                        "Rating"
                    )
                )

    st.divider()

    # =========================
    # DEPARTMENT ANALYTICS
    # =========================

    with st.container(border=True):

        st.subheader(
            "🏢 Department Performance Analytics"
        )

        dept_data = get_department_performance(
            company_id
        )

        if dept_data:

            dept_df = pd.DataFrame(
                dept_data,
                columns=[
                    "Department",
                    "Average Score"
                ]
            )

            st.bar_chart(
                dept_df.set_index(
                    "Department"
                )
            )

        else:

            st.warning(
                "No department data available."
            )

    st.divider()

    # =========================
    # QUICK INSIGHTS
    # =========================

    with st.container(border=True):

        st.subheader(
            "📌 Quick Insights"
        )

        if avg_score >= 85:

            st.success(
                "Overall employee performance is excellent."
            )

        elif avg_score >= 70:

            st.info(
                "Overall employee performance is good."
            )

        else:

            st.warning(
                "Overall employee performance needs improvement."
            )

        st.write(
            f"🏆 Top Performer: {top_performer[0] if top_performer else '-'}"
        )

        st.write(
            f"⭐ Employees Rated Excellent: {excellent_count}"
        )

        st.write(
            f"👨 Total Employees: {total_employees}"
        )

        st.write(
            f"📈 Average Performance Score: {avg_score}"
        )
