# streamlit_app.py
import streamlit as st
import sys, os

# Fix module paths for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import process_request
from app.notifier import send_whatsapp_reminder, post_announcement

# ---------- Session defaults ----------
if "users" not in st.session_state:
    st.session_state.users = {"andrewnarine": "ClassBot2025"}   # demo user
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""

# ---------- Page layout ----------
st.set_page_config(page_title="AlphaClassBot", layout="centered")
st.title("🎓 AlphaClassBot – Student Scheduler")

# ---------- Auth sidebar ----------
auth_choice = st.sidebar.radio("Choose Option", ["Sign In", "Sign Up"], key="auth_radio")

if not st.session_state.authenticated:

    # ---------- Sign-in ----------
    if auth_choice == "Sign In":
        st.subheader("🔐 Sign In")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Sign In", key="signin_btn"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"✅ Welcome, {username}!")
                st.rerun()                 # <-- changed
            else:
                st.error("❌ Invalid username or password.")

    # ---------- Sign-up ----------
    elif auth_choice == "Sign Up":
        st.subheader("📝 Sign Up")
        new_username = st.text_input("Choose a username", key="signup_username")
        new_password = st.text_input("Choose a password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm password", type="password", key="signup_confirm")

        if st.button("Create Account", key="signup_btn"):
            if new_username in st.session_state.users:
                st.warning("⚠️ Username already exists.")
            elif new_password != confirm_password:
                st.warning("⚠️ Passwords do not match.")
            elif not new_username or not new_password:
                st.warning("⚠️ All fields are required.")
            else:
                st.session_state.users[new_username] = new_password
                st.success("✅ Account created successfully! Please sign in.")
                st.rerun()                 # <-- changed

# ---------- Main app (after login) ----------
else:
    st.success(f"✅ Logged in as `{st.session_state.username}`")

    st.subheader("📅 Schedule a Request")
    user_input = st.text_input("Type your request (e.g. schedule, reminders, announcements)",
                               key="request_input")
    event      = st.text_input("Event name (optional)", key="event_input")
    date       = st.date_input("Event date (optional)", key="date_input")
    role       = "student"

    if st.button("Submit", key="submit_button"):
        response, status = process_request(user_input, role, event, str(date))
        {"error": st.error,
         "warning": st.warning,
         "info": st.info}.get(status, st.success)(response)

    if st.button("Send WhatsApp Reminder", key="reminder_button"):
        send_whatsapp_reminder(f"Reminder: {event} is on {date}")

    platform = st.selectbox("Choose Platform",
                            ["Facebook", "Instagram", "X/Twitter"],
                            key="platform_select")
    if st.button("Post Social Media Announcement", key="announce_button"):
        post_announcement(platform, f"📢 Don't miss: {event} on {date}!")

    if st.button("Log Out", key="logout_button"):
        st.session_state.authenticated = False
        st.session_state.username = ""
        st.rerun()                 # <-- changed

# ---------- Footer ----------
st.markdown("---")
st.caption("🛡️ Powered by ANADelta • AlphaClassBot © 2025")






