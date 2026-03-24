import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Air India HR Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================== CUSTOM CSS (Light + Air India Red Theme) ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    body {
        font-family: 'Inter', sans-serif;
        background: #f8f9fa;
    }

    .main .block-container {
        padding-top: 1rem;
        max-width: 1400px;
    }

    /* Header */
    .header {
        background: white;
        padding: 12px 24px;
        border-bottom: 4px solid #d71920;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    .logo {
        font-size: 28px;
        font-weight: 700;
        color: #d71920;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .nav a {
        margin: 0 20px;
        text-decoration: none;
        color: #333;
        font-weight: 500;
    }

    .user-info {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .avatar {
        width: 42px;
        height: 42px;
        background: #ddd;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }

    /* Chat Area */
    .chat-container {
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        height: 75vh;
        display: flex;
        flex-direction: column;
    }

    .chat-header {
        padding: 16px 24px;
        border-bottom: 1px solid #eee;
        font-weight: 600;
        font-size: 18px;
        color: #d71920;
    }

    .messages {
        flex: 1;
        padding: 20px;
        overflow-y: auto;
        background: #f8f9fa;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .message {
        max-width: 75%;
        padding: 14px 20px;
        border-radius: 18px;
        line-height: 1.5;
    }

    .user-msg {
        align-self: flex-end;
        background: #d71920;
        color: white;
        border-radius: 18px 18px 4px 18px;
    }

    .bot-msg {
        align-self: flex-start;
        background: white;
        border: 1px solid #ddd;
        color: #1a1a1a;
        border-radius: 18px 18px 18px 4px;
    }

    /* Right Panel */
    .right-panel {
        background: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        height: 75vh;
        overflow-y: auto;
    }

    .service-btn {
        width: 100%;
        padding: 16px 20px;
        margin-bottom: 12px;
        border-radius: 30px;
        border: 2px solid #d71920;
        background: white;
        color: #d71920;
        font-weight: 600;
        font-size: 15.5px;
        transition: all 0.2s;
    }

    .service-btn:hover {
        background: #d71920;
        color: white;
    }

    .service-btn.active {
        background: #d71920;
        color: white;
    }

    .quick-card {
        background: #f8f9fa;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 12px;
    }

    .stButton>button {
        border-radius: 30px;
        height: 52px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": "Hello Aarsh 👋 How can I assist you with HR matters today?"}
    ]

if "mode" not in st.session_state:
    st.session_state.mode = None

# ====================== HEADER ======================
st.markdown("""
<div class="header">
    <div class="logo">
        ✈️ AIR INDIA
    </div>
    <div style="display:flex; gap:30px; font-size:15px;">
        <a href="#">HR Policies</a>
        <a href="#">Leave</a>
        <a href="#">Grievance</a>
    </div>
    <div class="user-info">
        <div class="avatar">👨‍✈️</div>
        <div>
            <strong>Aarsh Khare</strong><br>
            <small style="color:#666;">Pilot • HRM Group 1</small>
        </div>
        <button style="background:#d71920;color:white;border:none;padding:8px 20px;border-radius:30px;font-weight:600;">
            Log out
        </button>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================== LAYOUT ======================
left_col, right_col = st.columns([3, 1.2])

with left_col:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="chat-header">🤖 Air India HR Assistant</div>', unsafe_allow_html=True)
    
    # Messages
    msg_container = st.container()
    with msg_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f'<div class="message user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="message bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

    # Input
    user_input = st.chat_input("Type your message...")

with right_col:
    st.markdown("### 👤 Aarsh Khare")
    st.caption("Senior First Officer | Pilot")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = [{"role": "bot", "content": "New conversation started. How can I help you?"}]
        st.session_state.mode = None
        st.rerun()

    st.markdown("---")
    st.markdown("### HR Services")

    col_btn = st.columns(1)

    if st.button("📘 HR Policy Info", key="hr_btn", use_container_width=True):
        st.session_state.mode = "hr"
        st.rerun()

    if st.button("✈️ Apply for Leave", key="leave_btn", use_container_width=True):
        st.session_state.mode = "leave"
        st.rerun()

    if st.button("⚠️ Raise Complaint", key="comp_btn", use_container_width=True):
        st.session_state.mode = "complaint"
        st.rerun()

    st.markdown("---")
    st.markdown("### Quick Info")

    st.markdown("""
    <div class="quick-card">
        <strong>Leave Balance</strong><br>
        <span style="font-size:28px;color:#d71920;">24 days</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="quick-card">
        <strong>Max Duty Hours</strong><br>
        40 hours / week
    </div>
    """, unsafe_allow_html=True)

# ====================== LOGIC ======================
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.mode == "hr":
        q = user_input.lower()
        if "leave" in q or "balance" in q:
            response = "You currently have **24 paid leave days** remaining (as of March 2026)."
        elif "hours" in q or "duty" in q:
            response = "Maximum duty hours are **40 per week** with mandatory rest periods."
        elif "fatigue" in q:
            response = "Your current fatigue level is at **62%** (safe zone)."
        else:
            response = "According to Air India HR policy..."
    elif st.session_state.mode == "leave":
        response = f"✅ Leave request received for **{user_input}**. Please fill the form on the right panel for full submission."
    elif st.session_state.mode == "complaint":
        response = "✅ Your complaint has been noted. HR will contact you within 48 hours."
    else:
        response = "Please select a service from the right panel to continue."

    st.session_state.messages.append({"role": "bot", "content": response})
    st.rerun()

# ====================== MODE-SPECIFIC FORMS ======================
if st.session_state.mode == "leave":
    with right_col:
        st.markdown("### ✈️ Apply for Leave")
        with st.form("leave_form"):
            leave_date = st.date_input("Leave Date", value=datetime(2026, 4, 5))
            reason = st.text_area("Reason for Leave", placeholder="Medical / Personal / Family emergency...")
            uploaded_file = st.file_uploader("Supporting Document (optional)", type=["pdf", "jpg", "png"])
            
            submitted = st.form_submit_button("Submit Leave Request", type="primary")
            if submitted:
                st.success("Leave request submitted successfully! You can check status in HR Portal.")
                st.session_state.messages.append({"role": "bot", "content": f"Leave request for **{leave_date}** has been submitted."})
                st.rerun()

elif st.session_state.mode == "complaint":
    with right_col:
        st.markdown("### ⚠️ Raise Complaint")
        with st.form("complaint_form"):
            category = st.selectbox("Category", ["Leave Delay", "Salary Issue", "Workload", "Others"])
            description = st.text_area("Describe your issue in detail", height=150)
            
            submitted = st.form_submit_button("Submit Complaint", type="primary")
            if submitted:
                st.success("Complaint logged! Reference #AI-HR-20260325-7842")
                st.session_state.messages.append({"role": "bot", "content": "Your complaint has been successfully registered."})
                st.rerun()
