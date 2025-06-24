# main.py – AlphaClassBot Main Logic
from app.security import check_permissions, enforce_safety_guard
from typing import Optional
from app.calendar_guard import handle_user_input

# Enable or disable content restrictions
SHOWCASE_MODE = True  # ✅ Set to False to enforce restrictions after demo

def process_request(user_input: str, role: str = "student", event: Optional[str] = None, date: Optional[str] = None):
    # ✅ Step 1: Check for unsafe words
    if not enforce_safety_guard(user_input):
        return "⚠️ Unsafe input. Assistance not allowed.", "error"

    # ✅ Step 2: Check user permissions (unless in showcase mode)
    if not SHOWCASE_MODE:
        if not check_permissions(role, "submit_homework"):
            return "❌ Homework answers are restricted.", "error"

    # ✅ Step 3: Process input normally
    result, status = handle_user_input(user_input, event, date)
    return result, status
