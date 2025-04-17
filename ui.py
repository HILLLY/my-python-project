import streamlit as st
from main import handle_taskgenie_query
from PIL import Image
import re

# ✅ Page Setup
st.set_page_config(page_title="TaskGenie", layout="wide")

# ✅ Animated Gradient + Glow Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        body, .stApp {
            font-family: 'Inter', sans-serif;
            background-color: #0f1117;
            color: #ffffff;
        }

        .title {
            font-size: 3em;
            font-weight: bold;
            background: linear-gradient(270deg, #00e5ff, #b388ff, #00e5ff);
            background-size: 600% 600%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientMove 8s ease infinite;
            text-align: center;
            margin-top: 1rem;
        }

        .subtitle {
            text-align: center;
            font-size: 1.3em;
            color: #a0cbe8;
            margin-bottom: 2rem;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .chat-bubble {
            background: rgba(43, 43, 60, 0.95);
            border-left: 5px solid #00e5ff;
            border-radius: 12px;
            padding: 1rem;
            margin: 0.7rem 0;
            box-shadow: 0 0 12px #00e5ff33;
        }

        .chat-title {
            font-weight: bold;
            color: #00f2ff;
            margin-bottom: 0.3rem;
        }

        .stTextArea textarea {
            background-color: #1e1f2e;
            color: #fff;
            border: 1px solid #00f0ff88;
            border-radius: 10px;
        }

        .stButton > button {
            background-color: #00e5ff;
            color: white;
            font-weight: bold;
            padding: 0.6rem 1.5rem;
            border-radius: 12px;
            border: none;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #00bcd4;
            box-shadow: 0px 0px 10px #00e5ff88;
        }

        .image-container {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }

        .taskgenie-image {
            max-width: 75%;
            border-radius: 12px;
            box-shadow: 0 0 20px #00e5ff33;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Utility: Format Web Results
def format_links(md):
    link_pattern = r"\[(.*?)\]\((.*?)\):\s*(.*)"
    matches = re.findall(link_pattern, md)
    if not matches:
        return "No valid links found."

    formatted_links = ""
    for i, (title, url, desc) in enumerate(matches, 1):
        snippet = desc.strip()[:200] + "..." if len(desc.strip()) > 200 else desc.strip()
        formatted_links += f"""🔗 **[{title}]({url})**  
{snippet}

"""
    return formatted_links

# ✅ App Title & Image
st.markdown("<div class='title'>🤖 TaskGenie</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Break complex goals into smart tasks using local AI + real-time research</div>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 📝 Enter Your Goal")
        goal = st.text_area("What do you want to accomplish?", placeholder="e.g., Build a task automation system", height=150)
        use_web = st.checkbox("🌐 Include Real-Time Web Research?", value=True)

        if st.button("🧠 Generate Tasks"):
            if goal.strip():
                with st.spinner("🧠 Thinking..."):
                    results = handle_taskgenie_query(goal, use_web=use_web)

                    # ✅ Task Breakdown
                    st.markdown("### ✅ Task Breakdown")
                    for i, task in enumerate(results.get("broken_tasks", []), 1):
                        st.markdown(f"""
                            <div class="chat-bubble">
                                <div class="chat-title">Task {i}:</div>
                                {task}
                            </div>
                        """, unsafe_allow_html=True)

                    # ✅ Task Plan
                    st.markdown("### 🗺️ Task Plan")
                    for i, step in enumerate(results.get("plan", []), 1):
                        st.markdown(f"""
                            <div class="chat-bubble">
                                <div class="chat-title">Step {i}:</div>
                                {step}
                            </div>
                        """, unsafe_allow_html=True)

                    # ✅ Execution Simulation
                    st.markdown("### 🛠️ Execution Simulation")
                    for i, result in enumerate(results.get("execution_results", []), 1):
                        st.markdown(f"""
                            <div class="chat-bubble">
                                <div class="chat-title">Sim {i}:</div>
                                {result}
                            </div>
                        """, unsafe_allow_html=True)

                    # ✅ Web Research Section
                    research = results.get("research", None)
                    if research and research != "No research needed for this goal.":
                        st.markdown("### 🌐 Web Research")
                        formatted = format_links(research)
                        st.markdown(formatted)
            else:
                st.warning("Please enter a goal first.")

    with col2:
        try:
            st.markdown("<div class='image-container'>", unsafe_allow_html=True)
            st.image("assets/tech.png", use_container_width=True, output_format="auto")
            st.markdown("</div>", unsafe_allow_html=True)
        except:
            st.warning("Tech image not found in assets folder.")

# ✅ Footer
st.markdown("---")
st.markdown(
    "<center><small>⚡ Powered by TinyLLaMA + DuckDuckGo | Built with 💻 Streamlit | by Ujjwal</small></center>",
    unsafe_allow_html=True
)
