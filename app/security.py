# security.py – AlphaClassBot Security Module

import streamlit as st

# App Header
st.title("🎓 Alpha ClassBot App")
st.write("Welcome! This is a student assistant for scheduling and reminders.")
st.write("Please log in to continue.")

# --- 🔐 Placeholder Login ---
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # This is a placeholder for real login verification
    st.success("✅ Logged in successfully (placeholder).")

# --- 🔒 Security Logic Placeholder ---
st.subheader("Security Features")
st.write("This module will handle user roles, permissions, and safety checks.")

# ✅ Define user permissions
def check_permissions(user_role: str, action: str) -> bool:
    """
    Placeholder permission logic.
    Returns False if students try restricted actions.
    """
    if user_role == "student" and action == "submit_homework":
        return False
    return True

# ✅ Showcase Mode Toggle
SHOWCASE_MODE = True  # 🔄 Set to False when restrictions should apply again

# ✅ Define safety guard function
def enforce_safety_guard(user_input: str) -> bool:
    """
    Blocks inappropriate or restricted content.
    Returns False if user_input contains any blocked keyword.
    """
    if SHOWCASE_MODE:
        return True  # ✅ Allow all inputs during demo/testing

    blocked_keywords = ["answer", "solve", "cheat", "hack", "homework"]
    return not any(keyword in user_input.lower() for keyword in blocked_keywords)

# ℹ️ Footer
st.write("🛡️ Security rules and restrictions are currently relaxed for demo purposes.")
st.write("🔄 Restrictions will be re-enabled after the showcase.")
