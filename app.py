import streamlit as st

st.set_page_config(layout="wide")

# -------------------------------
# 🎨 PREMIUM UI CSS
# -------------------------------
st.markdown("""
<style>

body {
    background-color: #f5f6fa;
}

/* Main container */
.block-container {
    padding-top: 2rem;
}

/* Header */
.header {
    font-size: 28px;
    font-weight: 700;
    color: #d71920;
}

/* Chat bubbles */
.user {
    background: #d71920;
    color: white;
    padding: 10px 14px;
    border-radius: 15px 15px 5px 15px;
    margin: 6px 0;
    width: fit-content;
    margin-left: auto;
}

.bot {
    background: #ffffff;
    border: 1px solid #ddd;
    padding: 10px 14px;
    border-radius: 15px 15px 15px 5px;
    margin: 6px 0;
    width: fit-content;
}

/* Cards */
.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #eee;
    margin-bottom: 12px;
}

/* Buttons */
.stButton button {
    border-radius: 20px;
    border: 1px solid #d71920;
    color: #d71920;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #d71920;
    color: white;
}

/* Input */
.stChatInput {
    position: fixed;
    bottom: 20px;
    left: 5%;
    right: 35%;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🧠 SESSION STATE
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = None

if "step" not in st.session_state:
    st.session_state.step = None

# -------------------------------
# 🔁 NEW CHAT
# -------------------------------
def reset_chat():
    st.session_state.messages = []
    st.session_state.mode = None
    st.session_state.step = None

# -------------------------------
# HEADER
# -------------------------------
st.markdown("<div class='header'>✈️ Air India HR Assistant</div>", unsafe_allow_html=True)
st.caption("HRM Group 1 • Internal HR System")

st.divider()

# -------------------------------
# LAYOUT (LEFT CHAT / RIGHT PANEL)
# -------------------------------
left, right = st.columns([2,1])

# ===============================
# 💬 LEFT SIDE (CHAT)
# ===============================
with left:

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='user'>👤 {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

    user_input = st.chat_input("Type your message...")

# ===============================
# 📋 RIGHT SIDE (HR PANEL)
# ===============================
with right:

    st.markdown("### 👤 Aarsh Khare")
    st.caption("Pilot")

    if st.button("➕ New Chat"):
        reset_chat()
        st.rerun()

    st.markdown("---")

    st.markdown("### HR Services")

    if st.button("📘 HR Policy Info"):
        st.session_state.mode = "hr"
        st.session_state.messages.append({"role":"bot","content":"Ask me anything about HR policies"})
        st.rerun()

    if st.button("✈️ Apply Leave"):
        st.session_state.mode = "leave"
        st.session_state.step = "name"
        st.session_state.messages.append({"role":"bot","content":"Enter your name"})
        st.rerun()

    if st.button("⚠️ Raise Complaint"):
        st.session_state.mode = "complaint"
        st.session_state.messages.append({"role":"bot","content":"Describe your issue"})
        st.rerun()

    st.markdown("---")

    st.markdown("### Quick Info")

    st.markdown("<div class='card'>📅 Leave Balance: 24 days</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>⏱ Max Work Hours: 40/week</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>⚠️ Fatigue Threshold: 85%</div>", unsafe_allow_html=True)

# -------------------------------
# 🤖 LOGIC
# -------------------------------
def hr_response(q):
    q = q.lower()
    if "leave" in q:
        return "Employees get 24 paid leaves, 12 sick leaves."
    if "hours" in q:
        return "Max 40 hours/week with mandatory rest."
    if "fatigue" in q:
        return "85% warning, 90% critical."
    return "Ask about leave, hours, fatigue, or policies."

def leave_flow(inp):
    if st.session_state.step == "name":
        st.session_state.name = inp
        st.session_state.step = "date"
        return "Enter leave date"

    elif st.session_state.step == "date":
        st.session_state.date = inp
        st.session_state.step = "reason"
        return "Enter reason"

    elif st.session_state.step == "reason":
        st.session_state.step = None
        return f"✅ Leave submitted for {st.session_state.name} on {st.session_state.date}"

def complaint_flow(inp):
    return "✅ Complaint submitted to HR"

# -------------------------------
# HANDLE INPUT
# -------------------------------
if user_input:

    st.session_state.messages.append({"role":"user","content":user_input})

    if st.session_state.mode == "hr":
        response = hr_response(user_input)

    elif st.session_state.mode == "leave":
        response = leave_flow(user_input)

    elif st.session_state.mode == "complaint":
        response = complaint_flow(user_input)

    else:
        response = "Please select a service from the right panel."

    st.session_state.messages.append({"role":"bot","content":response})

    st.rerun()
