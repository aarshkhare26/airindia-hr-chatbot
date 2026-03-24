import streamlit as st

st.set_page_config(page_title="Air India HR AI", layout="wide")

# -------------------------------
# HR POLICIES
# -------------------------------
HR_POLICIES = {
    "leave policy": """
Employees are entitled to:
• 24 paid leaves annually
• 12 sick leaves
• Emergency leave with approval
""",

    "working hours": """
• Max 40 hours/week
• 12-hour rest mandatory
• Weekly off compulsory
""",

    "fatigue policy": """
• 85% = warning
• 90% = HR intervention
• 100% = not allowed
""",

    "promotion policy": """
• Rating > 4.5
• Low delays
• High consistency
"""
}

# -------------------------------
# HEADER
# -------------------------------
st.markdown(
    """
    <h1 style='color:#d71920;'>✈️ Air India HR AI Assistant</h1>
    <h4>HRM Group 1</h4>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# SESSION STATE
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "leave_flow" not in st.session_state:
    st.session_state.leave_flow = None

# -------------------------------
# DISPLAY CHAT
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------------------
# INPUT
# -------------------------------
user_input = st.chat_input("Ask HR questions...")

# -------------------------------
# RESPONSE LOGIC
# -------------------------------
def generate_response(query):
    query = query.lower()

    if "leave policy" in query:
        return HR_POLICIES["leave policy"]

    elif "working hours" in query:
        return HR_POLICIES["working hours"]

    elif "fatigue" in query:
        return HR_POLICIES["fatigue policy"]

    elif "promotion" in query:
        return HR_POLICIES["promotion policy"]

    elif "hire" in query:
        return "Based on projections, hiring 3–5 pilots is recommended."

    elif "leave" in query:
        st.session_state.leave_flow = "name"
        return "Enter your name"

    else:
        return "I can help with HR policies, leave requests, and workforce insights."

# -------------------------------
# LEAVE FLOW
# -------------------------------
def handle_leave(user_input):
    if st.session_state.leave_flow == "name":
        st.session_state.name = user_input
        st.session_state.leave_flow = "dates"
        return "Enter leave dates"

    elif st.session_state.leave_flow == "dates":
        st.session_state.dates = user_input
        st.session_state.leave_flow = "reason"
        return "Enter reason"

    elif st.session_state.leave_flow == "reason":
        st.session_state.leave_flow = None
        return f"✅ Leave applied for {st.session_state.name} ({st.session_state.dates})"

# -------------------------------
# HANDLE CHAT
# -------------------------------
if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.leave_flow:
        response = handle_leave(user_input)
    else:
        response = generate_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)
