import streamlit as st
from datetime import date

st.set_page_config(page_title="Air India HR Assistant", layout="wide", initial_sidebar_state="collapsed")

# ====================== LIGHT RED THEME CSS (Matching your screenshot) ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    .stApp {
        background: #fff8f5;
    }

    /* Main Header - Exactly like screenshot */
    .header {
        background: white;
        padding: 12px 30px;
        border-bottom: 3px solid #d71920;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 8px rgba(215, 25, 32, 0.1);
    }

    .logo {
        font-size: 26px;
        font-weight: 700;
        color: #d71920;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .nav {
        display: flex;
        gap: 32px;
        font-size: 15px;
        font-weight: 500;
    }

    .nav a {
        color: #333;
        text-decoration: none;
    }

    .user-section {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .avatar {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
    }

    .logout-btn {
        background: #d71920;
        color: white;
        border: none;
        padding: 9px 24px;
        border-radius: 30px;
        font-weight: 600;
        cursor: pointer;
    }

    /* Main Content */
    .main {
        display: flex;
        height: calc(100vh - 78px);
        padding: 20px;
        gap: 20px;
    }

    /* Left Chat Area */
    .chat-area {
        flex: 2;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .chat-title {
        padding: 20px 24px;
        font-size: 22px;
        font-weight: 600;
        color: #1a1a1a;
        border-bottom: 1px solid #f0f0f0;
    }

    .messages {
        flex: 1;
        padding: 24px;
        overflow-y: auto;
        background: #fffaf7;
        display: flex;
        flex-direction: column;
        gap: 16px;
    }

    .message {
        max-width: 75%;
        padding: 14px 20px;
        border-radius: 18px;
        line-height: 1.5;
        font-size: 15.5px;
    }

    .user-msg {
        align-self: flex-end;
        background: #d71920;
        color: white;
        border-radius: 18px 18px 5px 18px;
    }

    .bot-msg {
        align-self: flex-start;
        background: #f1f1f1;
        color: #333;
        border-radius: 18px 18px 18px 5px;
    }

    /* Right Panel */
    .right-panel {
        flex: 1;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        padding: 24px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .service-btn {
        width: 100%;
        padding: 16px 20px;
        background: white;
        border: 2px solid #d71920;
        color: #d71920;
        border-radius: 30px;
        font-weight: 600;
        margin-bottom: 12px;
        transition: all 0.2s;
    }

    .service-btn:hover {
        background: #d71920;
        color: white;
    }

    .quick-card {
        background: #fff0eb;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": "Hi Aarsh! 👋<br><br>I am your **Air India HR Assistant**.<br>How can I help you today?"}
    ]

if "mode" not in st.session_state:
    st.session_state.mode = None

# ====================== HEADER ======================
st.markdown("""
<div class="header">
    <div class="logo">
        ✈️ AIR INDIA
    </div>
    <div class="nav">
        <a href="#">HR Policies</a>
        <a href="#">Leave</a>
        <a href="#">Grievance</a>
    </div>
    <div class="user-section">
        <div class="avatar">👨‍✈️</div>
        <div>
            <strong>Aarsh Khare</strong><br>
            <small style="color:#666;">Pilot • HRM Group 1</small>
        </div>
        <button class="logout-btn">Log out</button>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================== MAIN LAYOUT ======================
left, right = st.columns([2.2, 1])

with left:
    st.markdown('<div class="chat-area">', unsafe_allow_html=True)
    st.markdown('<div class="chat-title">Air India HR Chatbot</div>', unsafe_allow_html=True)

    # Messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="message user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

    user_input = st.chat_input("Type your message...")

with right:
    st.markdown("### 👤 Aarsh Khare")
    st.caption("Senior First Officer | Pilot")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = [{"role": "bot", "content": "Hi Aarsh! 👋 How can the HR Assistant help you today?"}]
        st.session_state.mode = None
        st.rerun()

    st.markdown("---")
    st.markdown("### HR Services")

    if st.button("📘 HR Policy Info", use_container_width=True, key="hr"):
        st.session_state.mode = "hr"
        st.session_state.messages.append({"role": "bot", "content": "Please ask any HR or policy related question."})
        st.rerun()

    if st.button("✈️ Apply for Leave", use_container_width=True, key="leave"):
        st.session_state.mode = "leave"
        st.session_state.messages.append({"role": "bot", "content": "Please fill the leave form on the right."})
        st.rerun()

    if st.button("⚠️ Raise Complaint", use_container_width=True, key="complaint"):
        st.session_state.mode = "complaint"
        st.session_state.messages.append({"role": "bot", "content": "Please describe your issue in the form."})
        st.rerun()

    st.markdown("---")
    st.markdown("### Quick Info")

    st.markdown("""
    <div class="quick-card">
        <strong>Leave Balance</strong><br>
        <span style="font-size: 26px; color:#d71920;">24 days</span>
    </div>
    """, unsafe_allow_html=True)

# ====================== LOGIC ======================
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.mode == "hr":
        response = "According to Air India HR policy..."
        if "leave" in user_input.lower():
            response = "You have **24 paid leave days** remaining."
    else:
        response = "Please select a service from the right panel."

    st.session_state.messages.append({"role": "bot", "content": response})
    st.rerun()

# ====================== FORMS IN RIGHT PANEL ======================
if st.session_state.mode == "leave":
    with right:
        st.markdown("### ✈️ Apply for Leave")
        with st.form("leave_form"):
            st.date_input("Leave Date", value=date(2026, 4, 5))
            st.text_area("Reason for Leave")
            st.file_uploader("Supporting Document (optional)")
            if st.form_submit_button("Submit Leave Request", type="primary"):
                st.success("✅ Leave request submitted successfully!")
                st.session_state.messages.append({"role": "bot", "content": "Your leave request has been submitted."})
                st.rerun()

elif st.session_state.mode == "complaint":
    with right:
        st.markdown("### ⚠️ Raise Complaint")
        with st.form("complaint_form"):
            st.selectbox("Category", ["Leave Delay", "Salary Issue", "Workload", "Other"])
            st.text_area("Describe your issue")
            if st.form_submit_button("Submit Complaint", type="primary"):
                st.success("✅ Complaint registered!")
                st.session_state.messages.append({"role": "bot", "content": "Your complaint has been logged."})
                st.rerun()
