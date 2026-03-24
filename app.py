import streamlit as st

st.set_page_config(page_title="Air India HR AI", layout="wide")

# -------------------------------
# THEME (PREMIUM UI)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #f8f9fa;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 2px solid #eee;
}

/* Header */
.title {
    color: #d71920;
    font-size: 32px;
    font-weight: bold;
}

/* Chat bubbles */
.user-bubble {
    background-color: #d71920;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px 0;
    text-align: right;
}

.bot-bubble {
    background-color: #ffffff;
    padding: 10px 15px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin: 5px 0;
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
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/4/4f/Air_India_Logo.svg", width=120)

    st.markdown("## ✈️ Air India HR AI")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.session_state.mode = None
        st.session_state.step = None
        st.rerun()

    st.markdown("---")
    st.write("👤 Logged in as: Aarsh")
    st.write("Role: Pilot")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("<div class='title'>✈️ Air India HR AI Assistant</div>", unsafe_allow_html=True)
st.write("HRM Group 1")

st.divider()

# -------------------------------
# STATE INIT
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = None

if "step" not in st.session_state:
    st.session_state.step = None

# -------------------------------
# START SCREEN
# -------------------------------
if st.session_state.mode is None:

    st.write("### 👇 Choose a service")

    col1, col2, col3 = st.columns(3)

    if col1.button("📘 HR Query"):
        st.session_state.mode = "hr"
        st.rerun()

    if col2.button("✈️ Apply Leave"):
        st.session_state.mode = "leave"
        st.session_state.step = "name"
        st.session_state.messages.append({"role": "bot", "content": "Enter your name"})
        st.rerun()

    if col3.button("⚠️ Complaint"):
        st.session_state.mode = "complaint"
        st.session_state.messages.append({"role": "bot", "content": "Describe your issue"})
        st.rerun()

    st.stop()

# -------------------------------
# DISPLAY CHAT
# -------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-bubble'>👤 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# -------------------------------
# INPUT
# -------------------------------
user_input = st.chat_input("Type your message...")

# -------------------------------
# LOGIC
# -------------------------------
def hr_response(q):
    q = q.lower()
    if "leave" in q:
        return "24 paid leaves, 12 sick leaves, emergency allowed."
    elif "hours" in q:
        return "Max 40 hrs/week, 12 hr rest mandatory."
    elif "fatigue" in q:
        return "85% warning, 90% critical."
    return "Ask about leave, hours, fatigue, or hiring."

def leave_flow(user_input):
    if st.session_state.step == "name":
        st.session_state.name = user_input
        st.session_state.step = "date"
        return "Enter leave date"

    elif st.session_state.step == "date":
        st.session_state.date = user_input
        st.session_state.step = "reason"
        return "Enter reason"

    elif st.session_state.step == "reason":
        st.session_state.step = None
        return f"✅ Leave submitted for {st.session_state.name} on {st.session_state.date}"

def complaint_flow(user_input):
    return "✅ Complaint submitted. HR will review."

# -------------------------------
# HANDLE INPUT
# -------------------------------
if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.mode == "hr":
        response = hr_response(user_input)

    elif st.session_state.mode == "leave":
        response = leave_flow(user_input)

    elif st.session_state.mode == "complaint":
        response = complaint_flow(user_input)

    st.session_state.messages.append({"role": "bot", "content": response})

    st.rerun()
