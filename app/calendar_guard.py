# Placeholder for scheduler.py
# calendar_guard.py
import re

INSTRUCTOR_CALENDAR = {
    "Math test": "2025-06-27",
    "Science quiz": "2025-07-01",
    "Final exam": "2025-08-10"
}

DANGEROUS_PATTERNS = [
    r"/inject", r"\bdelete\b", r"remind\(", r"\bshutdown\b",
    r"\bdrop\b", r"<script>", r"exec\(", r"system\(", r"\bimport\b"
]

def is_malicious_input(text: str) -> bool:
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in DANGEROUS_PATTERNS)

def sanitize_input(text):
    if is_malicious_input(text):
        return None, "⚠️ Sorry, that input isn't allowed."
    return text, None

def validate_event_date(event: str, date: str) -> bool:
    return INSTRUCTOR_CALENDAR.get(event) == date

def get_confirmation_prompt(event, date):
    if validate_event_date(event, date):
        return f"✅ Verified date for '{event}'. Confirm to save."
    return f"⚠️ This date doesn't match the official calendar. Continue anyway?"

def check_calendar(event):
    if event in INSTRUCTOR_CALENDAR:
        return f"📅 '{event}' is scheduled for {INSTRUCTOR_CALENDAR[event]}"
    return "❌ Event not found in instructor's calendar."

from typing import Optional

def handle_user_input(user_input: str, event: Optional[str] = None, date: Optional[str] = None):
    _, error = sanitize_input(user_input)
    if error:
        return error, "danger"

    if "save" in user_input.lower() and event and date:
        confirm_msg = get_confirmation_prompt(event, date)
        return f"Save '{event}' on {date}?\n{confirm_msg}", "warning"

    if "where" in user_input.lower() and "exam" in user_input.lower():
        return check_calendar("Final exam"), "info"

    return "✅ Task received. Awaiting confirmation if needed.", "success"


# notifier.py
# Replacing streamlit dependency with print for testability

def send_whatsapp_reminder(message: str):
    print(f"🔔 WhatsApp reminder would be: {message}")
    # Future: Integrate Twilio or WhatsApp API

def post_announcement(platform: str, message: str) -> None:
    print(f"📣 Announcement to {platform}: {message}")
    # Future: Link with Meta Graph API, Twitter API, etc.