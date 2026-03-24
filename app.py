import streamlit as st

st.set_page_config(page_title="Air India HR AI", layout="wide")

# -------------------------------
# CUSTOM CSS (THEME)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #ffffff;
}
.main {
    background-color: #ffffff;
}
h1 {
    color: #d71920;
}
.chat-user {
    background-color: #f5f5f5;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}
.chat-bot {
    background-color: #ffe6e6;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR (CHATGPT STYLE)
# -------------------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/4f/Air_India_Logo.svg/1200px-Air_India_Logo.svg.png", width=120)
    st.title("Air India HR AI")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.session_state.leave_flow = None
        st.rerun()

    st.markdown("---")
    st.write("### Chat History")
    st.write("• HR Query")
    st.write("• Leave Request")
    st.write("• Complaint")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1>✈️ Air India HR AI Assistant</h1>
<h4>HRM Group 1</h4>
""", unsafe_allow_html=True)

st.divider()

# -------------------------------
# INITIAL OPTIONS (BUTTONS)
# -------------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.write("### 👇 Choose a service")

    col1, col2, col3 = st.columns(3)

    if col1.button("📘 General HR Query"):
        st.session_state.started = True
        st.session_state.mode = "hr"

    if col2.button("✈️ Apply Leave"):
        st.session_state.started = True
        st.session_state.mode = "leave"
        st.session_state.leave_flow = "name"

    if col3.button("⚠️ Raise Complaint"):
        st.session_state.started = True
        st.session_state.mode = "complaint"

    st.stop()

# -------------------------------
# SESSION STATE
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "leave_flow" not in st.session_state:
    st.session_state.leave_flow = None

# -------------------------------
# HR POLICIES
# -------------------------------
HR_POLICIES = {
    "leave": "24 paid leaves, 12 sick leaves, emergency leave allowed.",
    "hours": "Max 40 hours/week, mandatory 12-hour rest.",
    "fatigue": "85% warning, 90% critical, 100% not allowed."
}

# -------------------------------
# DISPLAY CHAT
# -------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-user'>👤 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# -------------------------------
# INPUT
# -------------------------------
user_input = st.chat_input("Type your message...")

# -------------------------------
# RESPONSE LOGIC
# -------------------------------
def generate_response(query):
    query = query.lower()

    if "leave" in query:
        return HR_POLICIES["leave"]

    elif "hours" in query:
        return HR_POLICIES["hours"]

    elif "fatigue" in query:
        return HR_POLICIES["fatigue"]

    elif "hire" in query:
        return "Recommended hiring: 3–5 pilots based on demand."

    return "I can help with HR policies, leave requests, and workforce insights."

# -------------------------------
# LEAVE FLOW
# -------------------------------
def handle_leave(user_input):
    if st.session_state.leave_flow == "name":
        st.session_state.name = user_input
        st.session_state.leave_flow = "date"
        return "Enter leave date"

    elif st.session_state.leave_flow == "date":
        st.session_state.date = user_input
        st.session_state.leave_flow = None
        return f"✅ Leave applied for {st.session_state.name} on {st.session_state.date}"

# -------------------------------
# HANDLE INPUT
# -------------------------------
if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.leave_flow:
        response = handle_leave(user_input)
    else:
        response = generate_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()
