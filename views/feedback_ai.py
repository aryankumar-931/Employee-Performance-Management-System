import streamlit as st

from modules.employee import get_employee_names
from modules.performance import get_employee_performance
from modules.feedback import generate_feedback


def show_page():

    company_id = st.session_state.company_id

    st.title("🤖 AI Feedback Assistant")
    st.caption("AI-based employee performance insights")

    employees = get_employee_names(
        company_id
    )

    if not employees:

        st.warning(
            "No employees found."
        )

        return

    employee_names = [
        emp[1]
        for emp in employees
    ]

    selected_employee = st.selectbox(
        "Select Employee",
        employee_names
    )

    if st.button(
        "Generate AI Feedback"
    ):

        performance = get_employee_performance(
            selected_employee,
            company_id
        )

        if not performance:

            st.error(
                "No performance record found for this employee."
            )

            return

        attendance = performance[0]
        task_completion = performance[1]
        quality_score = performance[2]
        manager_feedback = performance[3]
        performance_score = performance[4]
        rating = performance[5]

        st.subheader(
            "📊 Performance Summary"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Performance Score",
                performance_score
            )

        with col2:

            st.metric(
                "Rating",
                rating
            )

        st.divider()

        strengths, improvements, recommendations = generate_feedback(
            attendance,
            task_completion,
            quality_score,
            manager_feedback
        )

        st.subheader("✅ Strengths")

        for item in strengths:

            st.success(item)

        st.subheader("⚠ Areas of Improvement")

        for item in improvements:

            st.warning(item)

        st.subheader("🚀 Recommendations")

        for item in recommendations:

            st.info(item)