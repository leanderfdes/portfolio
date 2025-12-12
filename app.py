import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Leander Fernandes | Portfolio",
    page_icon="💻",
    layout="wide"
)

# ---- HERO SECTION ----
st.title("👋 Hey, I'm Leander Fernandes")
st.write("### 💻 Computer Engineer | Full Stack Developer | AI Application Engineer")

st.write(
    "Computer Engineering graduate and aspiring **AI Application Engineer** with a strong foundation in "
    "full stack development and modern AI-powered systems. Experienced in building **production-grade web applications**, "
    "**RESTful APIs**, and **LLM-powered tools** using FastAPI, React, and cloud deployments. "
    "Passionate about designing clean, scalable, and user-centric software solutions that bridge "
    "backend systems with intelligent AI models. "
    "Completed an internship at **IBM SkillsBuild**, gaining hands-on experience in problem-solving, system thinking, "
    "and real-world application development. "
    "This portfolio showcases my projects, skills, and professional journey."
)

# ---- SOCIAL LINKS ----
st.markdown("---")
st.subheader("🌐 Connect with me:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[GitHub](https://github.com/leanderfdes)")
with col2:
    st.markdown("[LinkedIn](https://linkedin.com/in/leander22/)")
with col3:
    st.markdown("[Email Me](mailto:leanderfdes22@gmail.com)")

# ---- SKILLS SECTION ----
st.markdown("---")
st.subheader("🧠 Skills")
st.write(
    """
    - 💻 **Programming:** Python, JavaScript, C++  
    - 🌐 **Frontend:** React.js, Tailwind CSS, HTML, CSS  
    - ⚙️ **Backend:** FastAPI, Node.js, Express.js, REST APIs  
    - 🤖 **AI & LLMs:** Google Gemini API, Prompt Engineering, AI Integration  
    - 🗄️ **Databases:** MongoDB  
    - ☁️ **Deployment & DevOps:** Vercel, Render, Git, GitHub  
    - 🛠️ **Tools:** Postman, VS Code, Streamlit, Python-dotenv  
    """
)

# ---- PROJECTS SECTION ----
st.markdown("---")
st.subheader("🚀 Featured Projects")

# === PROJECT 1: LLM Playground (FLAGSHIP) ===
st.write(
    "### 🧠 1️⃣ LLM Playground — FastAPI + Gemini AI\n"
    "**🔗 Live Demo:** https://llm-playground-fastapi-gemini-nffi-ou4twwlmk.vercel.app/\n\n"
    "**🔗 GitHub Repo:** https://github.com/leanderfdes/llm-playground-fastapi-gemini\n\n"
    "A **production-grade AI application** that allows users to interact with a Large Language Model through a clean, "
    "modern web interface. Built with a **FastAPI backend** and a **React + Tailwind frontend**, "
    "this project demonstrates real-world AI application engineering.\n\n"
    "**Key Highlights:**\n"
    "- 🔹 FastAPI backend with clean architecture, logging, and error handling\n"
    "- 🔹 Google Gemini LLM integration with dynamic token control\n"
    "- 🔹 Modern React UI with typewriter animation and markdown rendering\n"
    "- 🔹 Prompt history, copy-to-clipboard, and dynamic example prompts\n"
    "- 🔹 Deployed using **Render (backend)** and **Vercel (frontend)**\n\n"
    "**Tech Stack:** FastAPI · Python · Google Gemini · React · Tailwind CSS · REST APIs · Vercel · Render"
)

# === PROJECT 2: To-Do App ===
st.write(
    "### ✅ 2️⃣ [To-Do List Web App](https://todo2list.netlify.app/)\n"
    "A responsive and minimal to-do list application built using **HTML, CSS, and JavaScript**. "
    "Focuses on clean UI, usability, and core frontend fundamentals.\n\n"
    "🔗 Live Demo: https://todo2list.netlify.app/"
)

# ---- FOOTER ----
st.markdown("---")
st.write("© 2025 Leander Fernandes | Made with ❤️ using Streamlit")
