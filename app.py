import streamlit as st

from database.db import create_table
from modules.auth import (
    login,
    register_admin
)

create_table()

st.set_page_config(
    page_title="Employee Performance System",
    page_icon="🚀",
    layout="wide"
)

# =========================
# Custom CSS
# =========================

st.markdown("""
<style>

.main > div {
    padding-top: 1rem;
}

div[data-testid="stMetric"] {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# Session State
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "company_id" not in st.session_state:
    st.session_state.company_id = None

if "company_name" not in st.session_state:
    st.session_state.company_name = ""

# =========================
# LOGIN / REGISTER
# =========================

if not st.session_state.logged_in:

    st.title("🚀 Employee Performance Management System")

    tab1, tab2 = st.tabs(
        [
            "🔐 Login",
            "📝 Register"
        ]
    )

    # =========================
    # LOGIN
    # =========================

    with tab1:

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            user = login(
                username,
                password
            )

            if user:

                st.session_state.logged_in = True

                st.session_state.company_id = user[0]
                st.session_state.company_name = user[1]
                st.session_state.username = user[2]

                st.success(
                    "✅ Login Successful"
                )

                st.rerun()

            else:

                st.error(
                    "❌ Invalid Username or Password"
                )

    # =========================
    # REGISTER
    # =========================

    with tab2:

        company_name = st.text_input(
            "Company Name"
        )

        username = st.text_input(
            "Username",
            key="register_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="register_pass"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Create Account"):

            if not company_name:

                st.error(
                    "Please enter company name."
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            else:

                success = register_admin(
                    company_name,
                    username,
                    password
                )

                if success:

                    st.success(
                        "✅ Account Created Successfully. Please Login."
                    )

                else:

                    st.error(
                        "❌ Username already exists."
                    )

# =========================
# MAIN APPLICATION
# =========================

else:

    st.sidebar.markdown("""
    # 🚀 EPMS

    ### Employee Performance
    Management System

    ---
    """)

    st.sidebar.success(
        f"🏢 {st.session_state.company_name}"
    )

    st.sidebar.caption(
        f"👤 {st.session_state.username}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.company_id = None
        st.session_state.company_name = ""

        st.rerun()

    page = st.sidebar.radio(
        "Go To",
        [
            "Employee Management",
            "Performance Analysis",
            "Dashboard",
            "Feedback AI",
            "Reports"
        ]
    )

    st.sidebar.markdown("---")
    #st.sidebar.caption("EPMS SaaS v4.0")

    if page == "Employee Management":
        from views.employee_management import show_page
        show_page()

    elif page == "Performance Analysis":
        from views.performance_analysis import show_page
        show_page()

    elif page == "Dashboard":
        from views.dashboard import show_page
        show_page()

    elif page == "Feedback AI":
        from views.feedback_ai import show_page
        show_page()

    elif page == "Reports":
        from views.reports import show_page
        show_page()

