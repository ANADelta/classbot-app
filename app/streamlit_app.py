# streamlit_app.py
import streamlit as st
import sys
import os

# Fix module paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import process_request
from app.notifier import send_whatsapp_reminder, post_announcement

# App config
st.set_page_config(page_title="AlphaClassBot", layout="centered")
st.title("🎓 AlphaClassBot – Student Scheduler")

# 👤 Login Fields
st.subheader("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# 🚀 Main app logic (only show if password is entered)
if username and password:
    st.success(f"Logged in as `{username}`")

    # 🗓️ Event Inputs
    st.subheader("Schedule a Request")
    user_input = st.text_input("Type your request (e.g. schedule, reminders, announcements)")
    event = st.text_input("Event name (optional)")
    date = st.date_input("Event date (optional)")
    role = "student"

    if st.button("Submit"):
        response, status = process_request(user_input, role, event, str(date))
        if status == "error":
            st.error(response)
        elif status == "warning":
            st.warning(response)
        elif status == "info":
            st.info(response)
        else:
            st.success(response)

    # 🔔 Reminder Button
    if st.button("Send WhatsApp Reminder"):
        send_whatsapp_reminder(f"Reminder: {event} is on {date}")

    # 📣 Social Media Announcement
    platform = st.selectbox("Choose Platform", ["Facebook", "Instagram", "X/Twitter"])
    if st.button("Post Social Media Announcement"):
        post_announcement(platform, f"📢 Don't miss: {event} on {date}!")
else:
    st.warning("Please enter both username and password to access the scheduler.")


