<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Air India HR Assistant</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;display=swap');

        :root {
            --air-red: #d71920;
            --air-dark: #1a1a1a;
            --air-light: #f8f9fa;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', system_ui, sans-serif;
            background: #f8f9fa;
            color: #1a1a1a;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        /* HEADER - exactly like the white/red screenshot */
        .header {
            background: white;
            border-bottom: 3px solid var(--air-red);
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 28px;
            font-weight: 700;
            color: var(--air-red);
            letter-spacing: -1px;
        }

        .logo span {
            font-size: 32px;
        }

        .nav {
            display: flex;
            gap: 32px;
            font-weight: 500;
            font-size: 15px;
        }

        .nav a {
            color: #333;
            text-decoration: none;
            transition: color 0.2s;
        }

        .nav a:hover {
            color: var(--air-red);
        }

        .user-section {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .user-avatar {
            width: 36px;
            height: 36px;
            background: #e6e6e6;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: #555;
        }

        .user-info {
            text-align: right;
        }

        .user-name {
            font-weight: 600;
            font-size: 15px;
        }

        .user-role {
            font-size: 13px;
            color: #666;
        }

        .logout-btn {
            background: var(--air-red);
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 30px;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .logout-btn:hover {
            background: #b0171a;
            transform: translateY(-1px);
        }

        /* MAIN CONTAINER */
        .main-container {
            flex: 1;
            display: flex;
            overflow: hidden;
        }

        /* LEFT CHAT AREA - ChatGPT style */
        .chat-area {
            flex: 3;
            display: flex;
            flex-direction: column;
            background: white;
            border-right: 1px solid #eee;
        }

        .chat-header {
            padding: 16px 24px;
            border-bottom: 1px solid #eee;
            font-weight: 600;
            font-size: 18px;
            display: flex;
            align-items: center;
            gap: 8px;
            background: white;
        }

        .messages {
            flex: 1;
            padding: 24px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 16px;
            background: #f8f9fa;
        }

        .message {
            max-width: 78%;
            padding: 14px 20px;
            border-radius: 20px;
            line-height: 1.5;
            font-size: 15.5px;
            position: relative;
        }

        .user-message {
            align-self: flex-end;
            background: var(--air-red);
            color: white;
            border-radius: 20px 20px 4px 20px;
        }

        .bot-message {
            align-self: flex-start;
            background: white;
            border: 1px solid #ddd;
            color: #1a1a1a;
            border-radius: 20px 20px 20px 4px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }

        .input-area {
            padding: 16px 24px;
            background: white;
            border-top: 1px solid #eee;
        }

        .chat-input {
            width: 100%;
            background: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 30px;
            padding: 14px 24px;
            font-size: 15px;
            outline: none;
            resize: none;
            height: 52px;
            display: flex;
            align-items: center;
        }

        .chat-input:focus {
            border-color: var(--air-red);
        }

        .send-btn {
            background: var(--air-red);
            color: white;
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            margin-left: 8px;
        }

        /* RIGHT PANEL - exactly like first screenshot but light theme */
        .right-panel {
            flex: 1;
            background: white;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 24px;
            overflow-y: auto;
            border-left: 1px solid #eee;
        }

        .user-card {
            display: flex;
            align-items: center;
            gap: 12px;
            padding-bottom: 16px;
            border-bottom: 1px solid #eee;
        }

        .new-chat-btn {
            background: white;
            color: var(--air-red);
            border: 2px solid var(--air-red);
            padding: 12px 24px;
            border-radius: 30px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .new-chat-btn:hover {
            background: var(--air-red);
            color: white;
        }

        .section-title {
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 12px;
        }

        .service-btn {
            width: 100%;
            padding: 14px 20px;
            margin-bottom: 12px;
            border-radius: 30px;
            border: 2px solid var(--air-red);
            background: white;
            color: var(--air-red);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 15px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .service-btn:hover {
            background: var(--air-red);
            color: white;
        }

        .service-btn.active {
            background: var(--air-red);
            color: white;
        }

        .quick-info {
            background: #f8f9fa;
            border-radius: 16px;
            padding: 20px;
        }

        .quick-card {
            background: white;
            border-radius: 12px;
            padding: 14px 18px;
            margin-bottom: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        /* Form styling for Leave & Complaint */
        .form-container {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 16px;
        }

        label {
            font-weight: 500;
            font-size: 14px;
            display: block;
            margin-bottom: 6px;
            color: #444;
        }

        .form-input {
            width: 100%;
            padding: 12px 16px;
            border: 1px solid #ddd;
            border-radius: 12px;
            font-size: 15px;
            margin-bottom: 16px;
        }

        .submit-btn {
            background: var(--air-red);
            color: white;
            border: none;
            width: 100%;
            padding: 14px;
            border-radius: 30px;
            font-weight: 600;
            font-size: 16px;
            cursor: pointer;
        }

        .success {
            animation: pop 0.3s;
        }

        @keyframes pop {
            0% { transform: scale(0.95); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>

    <!-- HEADER -->
    <div class="header">
        <div class="logo">
            <span>✈️</span>
            AIR INDIA
        </div>
        
        <div class="nav">
            <a href="#">HR Policies</a>
            <a href="#">Leave Management</a>
            <a href="#">Grievance Portal</a>
            <a href="#">My Profile</a>
        </div>

        <div class="user-section">
            <div class="user-avatar">👨‍✈️</div>
            <div class="user-info">
                <div class="user-name">Aarsh Khare</div>
                <div class="user-role">Pilot • HRM Group 1</div>
            </div>
            <button onclick="logout()" class="logout-btn">Log out</button>
        </div>
    </div>

    <div class="main-container">

        <!-- CHAT AREA -->
        <div class="chat-area">
            <div class="chat-header">
                <span id="chat-title">HR Assistant</span>
                <span style="margin-left:auto; font-size:13px; color:#666;" id="mode-indicator"></span>
            </div>

            <div class="messages" id="messages">
                <!-- Messages populated by JS -->
            </div>

            <div class="input-area">
                <div style="display:flex; align-items:center;">
                    <input 
                        id="user-input"
                        type="text" 
                        class="chat-input" 
                        placeholder="Type your message here... (HR questions only in Policy mode)"
                        onkeypress="if(event.key === 'Enter') sendMessage()">
                    <button onclick="sendMessage()" class="send-btn">↑</button>
                </div>
                <div style="text-align:center; margin-top:8px; font-size:12px; color:#777;">
                    Powered by Air India Internal AI • All data is confidential
                </div>
            </div>
        </div>

        <!-- RIGHT PANEL -->
        <div class="right-panel">

            <!-- User card -->
            <div class="user-card">
                <div class="user-avatar" style="width:52px;height:52px;font-size:24px;">👨‍✈️</div>
                <div>
                    <h3 style="margin:0;">Aarsh Khare</h3>
                    <p style="margin:0;color:#666;font-size:14px;">Pilot • Senior First Officer</p>
                </div>
            </div>

            <!-- New Chat -->
            <button onclick="newChat()" class="new-chat-btn">
                <span style="font-size:22px;">✚</span> 
                New Chat
            </button>

            <hr style="border:none; border-top:1px solid #eee;">

            <!-- HR Services -->
            <div class="section-title">HR Services</div>

            <button onclick="selectService('hr')" id="btn-hr" class="service-btn">
                📘 HR Policy Info
            </button>
            <button onclick="selectService('leave')" id="btn-leave" class="service-btn">
                ✈️ Apply for Leave
            </button>
            <button onclick="selectService('complaint')" id="btn-complaint" class="service-btn">
                ⚠️ Raise Complaint
            </button>

            <hr style="border:none; border-top:1px solid #eee;">

            <!-- Dynamic Content Area -->
            <div id="dynamic-content">

                <!-- Default Quick Info (shown initially) -->
                <div id="quick-info">
                    <div class="section-title">Quick Info</div>
                    <div class="quick-card">
                        <span style="font-size:28px;">📅</span>
                        <div>
                            <strong>Leave Balance</strong><br>
                            <span style="font-size:24px;color:var(--air-red);">24 days</span>
                        </div>
                    </div>
                    <div class="quick-card">
                        <span style="font-size:28px;">⏰</span>
                        <div>
                            <strong>Max Work Hours</strong><br>
                            40 hours / week
                        </div>
                    </div>
                    <div class="quick-card">
                        <span style="font-size:28px;">⚠️</span>
                        <div>
                            <strong>Fatigue Threshold</strong><br>
                            85% — You are currently at <strong style="color:var(--air-red);">62%</strong>
                        </div>
                    </div>
                </div>

                <!-- Leave Form (hidden by default) -->
                <div id="leave-form" style="display:none;">
                    <div class="section-title">Apply for Leave</div>
                    <div class="form-container">
                        <label>Leave Start Date</label>
                        <input type="date" id="leave-date" class="form-input" value="2026-04-05">

                        <label>Reason for Leave</label>
                        <textarea id="leave-reason" class="form-input" rows="3" placeholder="Medical / Personal / Training..."></textarea>

                        <label>Supporting Document (optional)</label>
                        <input type="file" id="leave-file" accept=".pdf,.jpg,.png" style="margin-bottom:20px;width:100%;">

                        <button onclick="submitLeave()" class="submit-btn">Submit Leave Request</button>
                        <p style="text-align:center;font-size:13px;margin-top:12px;color:#666;">
                            Request will be sent to your reporting manager
                        </p>
                    </div>
                </div>

                <!-- Complaint Form -->
                <div id="complaint-form" style="display:none;">
                    <div class="section-title">Raise a Complaint</div>
                    <div class="form-container">
                        <label>Category</label>
                        <select id="complaint-category" class="form-input">
                            <option>Leave Approval Delay</option>
                            <option>Salary Issue</option>
                            <option>Workload / Fatigue</option>
                            <option>Other</option>
                        </select>

                        <label>Detailed Description</label>
                        <textarea id="complaint-desc" class="form-input" rows="5" placeholder="Please describe your issue in detail..."></textarea>

                        <button onclick="submitComplaint()" class="submit-btn">Submit Complaint</button>
                        <p style="text-align:center;font-size:13px;margin-top:12px;color:#666;">
                            HR will respond within 48 hours
                        </p>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <script>
        // Session state
        let messages = [
            {
                role: "bot",
                content: "Hello Aarsh 👋 Welcome back! How can I help you with HR today?"
            }
        ];

        let currentMode = null;

        // Render messages
        function renderMessages() {
            const container = document.getElementById("messages");
            container.innerHTML = "";

            messages.forEach(msg => {
                const div = document.createElement("div");
                div.className = msg.role === "user" ? "message user-message" : "message bot-message";
                div.innerHTML = `
                    ${msg.role === "bot" ? `<strong style="color:#d71920;">🤖 Air India HR</strong><br>` : ''}
                    ${msg.content}
                `;
                container.appendChild(div);
            });

            // Scroll to bottom
            container.scrollTop = container.scrollHeight;
        }

        // Send message (only works in HR Policy mode)
        function sendMessage() {
            const input = document.getElementById("user-input");
            const text = input.value.trim();

            if (!text) return;

            // Add user message
            messages.push({ role: "user", content: text });
            renderMessages();

            // Clear input
            input.value = "";

            // Only respond if in HR mode
            if (currentMode === "hr") {
                setTimeout(() => {
                    let reply = "Thank you for your question. Here is the official policy information.";

                    if (text.toLowerCase().includes("leave") || text.toLowerCase().includes("balance")) {
                        reply = "✅ You currently have <strong>24 paid leave days</strong> remaining (as of March 2026).";
                    } else if (text.toLowerCase().includes("policy") || text.toLowerCase().includes("sick")) {
                        reply = "Sick leave: Up to 12 days per year. Medical certificate required for >3 days.";
                    } else if (text.toLowerCase().includes("hours") || text.toLowerCase().includes("fatigue")) {
                        reply = "Maximum duty hours per week: 40. Fatigue threshold alert at 85%.";
                    }

                    messages.push({ role: "bot", content: reply });
                    renderMessages();
                }, 800);
            } else {
                setTimeout(() => {
                    messages.push({
                        role: "bot",
                        content: "Please use the form on the right panel for Leave or Complaint requests. For HR policy questions, select <strong>HR Policy Info</strong> first."
                    });
                    renderMessages();
                }, 600);
            }
        }

        // Select service
        function selectService(mode) {
            currentMode = mode;
            document.getElementById("mode-indicator").innerHTML = 
                mode === "hr" ? "📘 Policy Mode" : 
                mode === "leave" ? "✈️ Leave Application" : "⚠️ Complaint";

            // Highlight active button
            document.querySelectorAll(".service-btn").forEach(btn => btn.classList.remove("active"));
            if (mode === "hr") document.getElementById("btn-hr").classList.add("active");
            if (mode === "leave") document.getElementById("btn-leave").classList.add("active");
            if (mode === "complaint") document.getElementById("btn-complaint").classList.add("active");

            // Show correct form / quick info
            document.getElementById("quick-info").style.display = mode === "hr" ? "block" : "none";
            document.getElementById("leave-form").style.display = mode === "leave" ? "block" : "none";
            document.getElementById("complaint-form").style.display = mode === "complaint" ? "block" : "none";

            // Welcome message for each mode
            if (mode === "hr") {
                messages.push({ role: "bot", content: "Ask me anything about HR policies, leave balance, working hours, or benefits." });
            } else if (mode === "leave") {
                messages.push({ role: "bot", content: "Please fill the leave form on the right. I’ll confirm once submitted." });
            } else if (mode === "complaint") {
                messages.push({ role: "bot", content: "Describe your issue in the form. All complaints are handled confidentially." });
            }

            renderMessages();
        }

        // Submit Leave
        function submitLeave() {
            const date = document.getElementById("leave-date").value;
            const reason = document.getElementById("leave-reason").value || "No reason provided";

            messages.push({
                role: "bot",
                content: `✅ Leave request submitted successfully!<br><br>Date: <strong>${date}</strong><br>Reason: ${reason}<br><br>You can track status in the HR portal.`
            });

            renderMessages();

            // Reset form and return to quick info
            setTimeout(() => {
                document.getElementById("leave-form").style.display = "none";
                document.getElementById("quick-info").style.display = "block";
                currentMode = null;
                document.getElementById("mode-indicator").innerHTML = "";
                document.querySelectorAll(".service-btn").forEach(b => b.classList.remove("active"));
            }, 1800);
        }

        // Submit Complaint
        function submitComplaint() {
            const desc = document.getElementById("complaint-desc").value || "No description";

            messages.push({
                role: "bot",
                content: `⚠️ Complaint logged successfully!<br><br><strong>Reference #AI-HR-2026-${Math.floor(Math.random()*9999)}</strong><br>HR team will review within 48 hours.`
            });

            renderMessages();

            setTimeout(() => {
                document.getElementById("complaint-form").style.display = "none";
                document.getElementById("quick-info").style.display = "block";
                currentMode = null;
                document.getElementById("mode-indicator").innerHTML = "";
                document.querySelectorAll(".service-btn").forEach(b => b.classList.remove("active"));
            }, 1800);
        }

        // New Chat
        function newChat() {
            messages = [
                { role: "bot", content: "New chat started. How can the Air India HR Assistant help you today?" }
            ];
            currentMode = null;
            document.getElementById("mode-indicator").innerHTML = "";
            document.querySelectorAll(".service-btn").forEach(b => b.classList.remove("active"));
            document.getElementById("quick-info").style.display = "block";
            document.getElementById("leave-form").style.display = "none";
            document.getElementById("complaint-form").style.display = "none";
            renderMessages();
        }

        // Fake logout
        function logout() {
            if (confirm("Log out of Air India HR Assistant?")) {
                window.location.reload();
            }
        }

        // Initial render
        window.onload = function() {
            renderMessages();
        };
    </script>
</body>
</html>
